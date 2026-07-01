from fastapi import APIRouter
from pydantic import BaseModel

from app.services.openai_service import ask_gpt
from app.services.analytics_service import (
    get_top_products,
    get_worst_product,
)
router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def chat(req: ChatRequest):

    message = req.message.lower()

    if "کم فروش" in message or "کم‌فروش" in message:

        worst = get_worst_product()

        prompt = f"""
کاربر پرسیده:
{req.message}

کم‌فروش‌ترین محصول:

نام محصول:
{worst["product"]}

مبلغ فروش:
{worst["sales"]}

در نقش یک مشاور کسب‌وکار،
به فارسی،
خیلی کوتاه و مفید پاسخ بده.
"""

    return {
        "reply": ask_gpt(prompt)
    }
    if "پرفروش" in message or "محصول" in message:

        top = get_top_products(1)[0]

        prompt = f"""
کاربر پرسیده:
{req.message}

اطلاعات فروش:

پرفروش‌ترین محصول:
{top['product']}

مبلغ فروش:
{top['sales']}

در قالب یک مشاور کسب‌وکار حرفه‌ای،
به فارسی،
خیلی کوتاه و مفید پاسخ بده.
"""

        return {
            "reply": ask_gpt(prompt)
        }

    return {
        "reply": ask_gpt(req.message)
    }
