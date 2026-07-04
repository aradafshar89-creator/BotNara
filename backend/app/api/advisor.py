from fastapi import APIRouter

from app.services.ai_advisor import generate_ai_advice

router = APIRouter()


@router.get("/advisor")
def advisor():

    return {

        "advice": generate_ai_advice()

    }
