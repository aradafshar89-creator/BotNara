from app.services.intent_service import detect_intent
from app.services.openai_service import ask_gpt
from app.services.analytics_service import (
    get_top_products,
    get_worst_product,
)


def process_message(message: str):

    intent = detect_intent(message)

    if intent == "TOP_PRODUCT":

        top = get_top_products()[0]

        prompt = f"""
کاربر پرسیده:
{message}

پرفروش‌ترین محصول:

نام محصول:
{top["product"]}

مبلغ فروش:
{top["sales"]}

در نقش یک مشاور حرفه‌ای کسب‌وکار،
خیلی کوتاه و فارسی پاسخ بده.
"""

        return ask_gpt(prompt)

    if intent == "WORST_PRODUCT":

        worst = get_worst_product()

        prompt = f"""
کاربر پرسیده:
{message}

کم‌فروش‌ترین محصول:

نام محصول:
{worst["product"]}

مبلغ فروش:
{worst["sales"]}

در نقش مشاور کسب‌وکار،
راهکار کوتاه ارائه بده.
"""

        return ask_gpt(prompt)

    return ask_gpt(message)
