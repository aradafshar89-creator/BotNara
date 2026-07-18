from fastapi import APIRouter, Depends

from app.auth.auth import get_current_user
from app.auth.models import User

from app.services.analytics_service import (
    get_monthly_sales,
    get_top_customers,
    get_top_products,
    get_profit_summary,
    get_worst_product,
)

router = APIRouter()


@router.get("/monthly-sales")
def monthly_sales(
    current_user: User = Depends(get_current_user),
):
    return get_monthly_sales(current_user)


@router.get("/top-customers")
def top_customers(
    current_user: User = Depends(get_current_user),
):
    return get_top_customers(current_user)


@router.get("/top-products")
def top_products(
    current_user: User = Depends(get_current_user),
):
    return get_top_products(current_user)


@router.get("/profit")
def profit(
    current_user: User = Depends(get_current_user),
):
    return get_profit_summary(current_user.company_id)


@router.get("/worst-product")
def worst_product(
    current_user: User = Depends(get_current_user),
):
    return get_worst_product(current_user.company_id)
@router.get("/dashboard")
def dashboard(
    current_user: User = Depends(get_current_user),
):
    return {
        "monthly_sales": get_monthly_sales(current_user),
        "top_customers": get_top_customers(current_user),
        "top_products": get_top_products(current_user),
        "profit": get_profit_summary(current_user.company_id),
        "worst_product": get_worst_product(current_user.company_id),
    }
