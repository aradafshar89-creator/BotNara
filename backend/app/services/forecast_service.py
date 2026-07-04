from app.services.analytics_service import get_monthly_sales

from app.services.openai_service import ask_gpt


def forecast_sales():

    monthly = get_monthly_sales()

    prompt = f"""
تو یک تحلیلگر ارشد فروش هستی.

فروش ماهانه شرکت:

{monthly}

بر اساس این داده‌ها:

1- روند فروش را تحلیل کن.

2- فروش ماه آینده را پیش‌بینی کن.

3- اگر افت فروش وجود دارد هشدار بده.

4- اگر رشد فروش وجود دارد پیشنهاد توسعه بده.

پاسخ را مدیریتی و کوتاه بنویس.
"""

    return ask_gpt(prompt)
