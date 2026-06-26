from sqlalchemy import func
from app.db.database import SessionLocal
from app.models.sale import Sale


def get_monthly_sales():

    db = SessionLocal()

    sales = db.query(Sale).all()

    result = {}

    for sale in sales:

        if sale.sale_date is None:
            continue

        month = sale.sale_date.strftime("%Y-%m")

        result[month] = result.get(month, 0) + sale.sale_amount

    db.close()

    return result
def get_top_customers(limit=10):

    db = SessionLocal()

    result = (
        db.query(
            Sale.customer,
            func.sum(Sale.sale_amount).label("sales")
        )
        .group_by(Sale.customer)
        .order_by(func.sum(Sale.sale_amount).desc())
        .limit(limit)
        .all()
    )

    db.close()

    return [
        {
            "customer": row.customer,
            "sales": float(row.sales)
        }
        for row in result
    ]

def get_top_products(limit=10):

    db = SessionLocal()

    sales = db.query(Sale).all()

    products = {}

    for sale in sales:

        products[sale.product] = (
            products.get(sale.product, 0)
            + sale.sale_amount
        )

    db.close()

    result = sorted(
        products.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return [
        {
            "product": name,
            "sales": amount
        }
        for name, amount in result[:limit]
    ]

def get_profit_summary():

    db = SessionLocal()

    sales = db.query(Sale).all()

    total_sales = sum((s.sale_amount or 0) for s in sales)

    total_purchase = sum((s.purchase_price or 0) for s in sales)

    total_profit = sum((s.profit or 0) for s in sales)

    margin = 0

    if total_sales > 0:
        margin = round((total_profit / total_sales) * 100, 2)

    db.close()

    return {
        "total_sales": total_sales,
        "total_purchase": total_purchase,
        "total_profit": total_profit,
        "margin_percent": margin
    }
def get_top_products(limit=10):

    db = SessionLocal()

    sales = db.query(Sale).all()

    products = {}

    for sale in sales:

        if not sale.product:
            continue

        products[sale.product] = (
            products.get(sale.product, 0)
            + sale.sale_amount
        )

    db.close()

    result = sorted(
        products.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return [
        {
            "product": name,
            "sales": amount,
        }
        for name, amount in result[:limit]
    ]
