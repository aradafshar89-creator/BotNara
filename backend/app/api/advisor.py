from fastapi import APIRouter

from app.services.advisor_service import generate_business_advice

router = APIRouter()


@router.get("/advisor")
def advisor():

    return {
        "advice": generate_business_advice()
    }
