from fastapi import APIRouter

from app.services.forecast_service import forecast_sales

router = APIRouter()


@router.get("/forecast")
def forecast():

    return {
        "forecast": forecast_sales()
    }
