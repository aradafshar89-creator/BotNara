from app.services.analytics_service import get_top_products
from app.services.analytics_service import get_top_customers
from app.services.analytics_service import get_monthly_sales


def ask_bot(message: str):

    text = message.lower()

    if "محصول" in text:

        products = get_top_products()

        if products:
            p = products[0]

            return (
                f"پرفروش‌ترین محصول "
                f"{p['product']} "
                f"با فروش "
                f"{p['sales']:,.0f} تومان است."
            )

    if "مشتری" in text:

        customers = get_top_customers()

        if customers:
            c = customers[0]

            return (
                f"بهترین مشتری "
                f"{c['customer']} "
                f"با خرید "
                f"{c['sales']:,.0f} تومان است."
            )

    if "ماه" in text:

        months = get_monthly_sales()

        return months

    return (
        "متوجه سؤال نشدم.\n"
        "مثلاً بپرس:\n"
        "پرفروش‌ترین محصول چیست؟"
    )
