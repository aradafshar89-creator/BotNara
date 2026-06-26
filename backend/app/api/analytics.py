from fastapi import APIRouter

from app.services.analytics_service import get_monthly_sales

from app.services.analytics_service import get_top_customers

from app.services.analytics_service import get_top_products

from app.services.analytics_service import get_profit_summary

router = APIRouter()


@router.get("/monthly-sales")
def monthly_sales():
    return get_monthly_sales()
@router.get("/top-customers")
def top_customers():
    return get_top_customers()
@router.get("/top-products")
def top_products():
    return get_top_products()
@router.get("/profit")
def profit():
    return get_profit_summary()
