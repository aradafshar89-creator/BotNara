from app.auth.models import User
from sqlalchemy import func
from app.db.database import SessionLocal
from app.models.sale import Sale


def get_monthly_sales(current_user: User):

    db = SessionLocal()

    try:

        sales = (
    db.query(Sale)
    .filter(
        Sale.company_id == current_user.company_id
    )
    .all()
)

        result = {}

        for sale in sales:

            if sale.sale_date is None:
                continue

            month = sale.sale_date.strftime("%Y-%m")

            result[month] = (
                result.get(month, 0)
                + sale.sale_amount
            )

        return result

    finally:
        db.close()


def get_top_customers(current_user: User, limit=10):

    db = SessionLocal()

    try:

        result = (
    db.query(
        Sale.customer,
        func.sum(Sale.sale_amount).label("sales")
    )
    .filter(
        Sale.company_id == current_user.company_id
    )
            .group_by(Sale.customer)
            .order_by(func.sum(Sale.sale_amount).desc())
            .limit(limit)
            .all()
        )

        return [
            {
                "customer": row.customer,
                "sales": float(row.sales)
            }
            for row in result
        ]

    finally:
        db.close()


def get_top_products(current_user: User, limit=10):

    db = SessionLocal()

    try:

        sales = (
            db.query(Sale)
            .filter(
                Sale.company_id == current_user.company_id
            )
            .all()
        )

        products = {}

        for sale in sales:

            if not sale.product:
                continue

            products[sale.product] = (
                products.get(sale.product, 0)
                + sale.sale_amount
            )

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

    finally:
        db.close()


def get_profit_summary(company_id):

    db = SessionLocal()

    try:

        sales = (
            db.query(Sale)
            .filter(Sale.company_id == company_id)
            .all()
        )

        total_sales = sum(
            (s.sale_amount or 0)
            for s in sales
        )

        total_purchase = sum(
            (s.purchase_price or 0)
            * (s.quantity or 1)
            for s in sales
        )

        total_profit = sum(
            (s.sale_amount or 0)
            -
            (
                (s.purchase_price or 0)
                * (s.quantity or 1)
            )
            for s in sales
        )

        margin = 0

        if total_sales > 0:

            margin = round(
                (total_profit / total_sales) * 100,
                2
            )

        return {
            "total_sales": total_sales,
            "total_purchase": total_purchase,
            "total_profit": total_profit,
            "margin_percent": margin
        }

    finally:
        db.close()


def get_worst_product(company_id):

    db = SessionLocal()

    try:

        result = (
            db.query(
                Sale.product,
                func.sum(Sale.sale_amount).label("sales")
            )
            .filter(Sale.company_id == company_id)
            .group_by(Sale.product)
            .order_by(func.sum(Sale.sale_amount).asc())
            .first()
        )

        if not result:
            return None

        return {
            "product": result.product,
            "sales": float(result.sales)
        }

    finally:
        db.close()
