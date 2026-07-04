from app.services.analytics_service import (
    get_top_products,
    get_worst_product,
    get_profit_summary,
)

from app.services.openai_service import ask_gpt


def generate_ai_advice():

    top = get_top_products(3)

    worst = get_worst_product()

    profit = get_profit_summary()

    prompt = f"""
تو مدیر فروش حرفه‌ای هستی.

اطلاعات شرکت:

پرفروش‌ترین محصولات:
{top}

کم‌فروش‌ترین محصول:
{worst}

خلاصه سود:
{profit}

در 5 جمله کوتاه و مدیریتی تحلیل کن.

فقط پیشنهاد مدیریتی بده.
"""

    return ask_gpt(prompt)
