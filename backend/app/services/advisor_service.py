from app.services.analytics_service import (
    get_top_products,
    get_worst_product,
    get_profit_summary,
)


def generate_business_advice():

    advice = []

    top = get_top_products()[0]

    worst = get_worst_product()

    profit = get_profit_summary()

    advice.append(
        f"🏆 پرفروش‌ترین محصول شما {top['product']} است."
    )

    advice.append(
        f"⚠️ کم‌فروش‌ترین محصول {worst['product']} است."
    )

    advice.append(
        f"💰 سود کل شما {profit['total_profit']:,.0f} تومان است."
    )

    return advice
