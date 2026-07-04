from app.services.analytics_service import (
    get_profit_summary,
    get_top_products,
    get_top_customers,
    get_monthly_sales,
)


def build_company_context():

    return {

        "profit": get_profit_summary(),

        "top_products": get_top_products(10),

        "top_customers": get_top_customers(10),

        "monthly_sales": get_monthly_sales(),

    }
