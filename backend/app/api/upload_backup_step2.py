from fastapi import APIRouter, UploadFile, File
import pandas as pd
import tempfile

from app.db.database import SessionLocal
from app.models.upload import Upload

router = APIRouter()


@router.get("/upload")
def get_uploads():
    db = SessionLocal()

    uploads = db.query(Upload).order_by(Upload.id.desc()).all()

    result = []

    for item in uploads:
        result.append({
            "id": item.id,
            "filename": item.filename,
            "upload_date": item.upload_date,
            "total_sales": item.total_sales,
            "total_orders": item.total_orders,
            "top_customer": item.top_customer,
            "top_product": item.top_product
        })

    db.close()

    return result
def find_column(columns, keywords):
    for col in columns:

        col_lower = col.lower().strip()

        for keyword in keywords:

            if keyword.lower() in col_lower:
                return col

    return None
@router.post("/upload")
async def upload_excel(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx") as tmp:
        content = await file.read()
        tmp.write(content)
        tmp_path = tmp.name

    df = pd.read_excel(tmp_path)

    amount_keywords = [
    "amount",
    "price",
    "total",
    "sale",
    "sales",
    "مبلغ",
    "فروش",
    "جمع",
    "جمع فروش",
    "قیمت",
    "قیمت نهایی",
    "مبلغ کل",
    "مبلغ نهایی"
    ]

    customer_keywords = [
    "customer",
    "client",
    "buyer",
    "customer name",
    "مشتری",
    "خریدار",
    "نام مشتری",
    "طرف حساب"
    ]

    product_keywords = [
    "product",
    "item",
    "sku",
    "product name",
    "کالا",
    "محصول",
    "نام کالا",
    "نام محصول"
    ]

    amount_col = find_column(df.columns, amount_keywords)
    customer_col = find_column(df.columns, customer_keywords)
    product_col = find_column(df.columns, product_keywords)

    if not amount_col:
        return {"error": "Amount column not found"}

    if not customer_col:
        return {"error": "Customer column not found"}

    if not product_col:
        return {"error": "Product column not found"}

    df[amount_col] = (
    df[amount_col]
    .astype(str)
    .str.replace("تومان", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.replace("۰", "0")
    .str.replace("۱", "1")
    .str.replace("۲", "2")
    .str.replace("۳", "3")
    .str.replace("۴", "4")
    .str.replace("۵", "5")
    .str.replace("۶", "6")
    .str.replace("۷", "7")
    .str.replace("۸", "8")
    .str.replace("۹", "9")
    )

    df[amount_col] = pd.to_numeric(df[amount_col],errors="coerce").fillna(0)

    total_sales = float(df[amount_col].sum())
    total_orders = len(df)

    top_customer = (
    df.groupby(customer_col)[amount_col]
    .sum()
    .idxmax()
    )

    top_product = (
        df.groupby(product_col)[amount_col]
        .sum()
        .idxmax()
    )

    db = SessionLocal()

    upload = Upload(
    filename=file.filename,
    total_sales=total_sales,
    total_orders=total_orders,
    top_customer=top_customer,
    top_product=top_product
    )

    db.add(upload)
    db.commit()
    db.refresh(upload)
    db.close()

    return {
    "id": upload.id,
    "filename": file.filename,
    "total_sales": total_sales,
    "total_orders": total_orders,
    "top_customer": top_customer,
    "top_product": top_product
    }
