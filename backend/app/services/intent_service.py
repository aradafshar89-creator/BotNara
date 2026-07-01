def detect_intent(message: str):

    text = message.lower()

    if "کم فروش" in text or "کم‌فروش" in text:
        return "WORST_PRODUCT"

    if "پرفروش" in text:
        return "TOP_PRODUCT"

    if "مشتری" in text:
        return "TOP_CUSTOMER"

    if "سود" in text:
        return "PROFIT"

    if "ماهانه" in text or "فروش ماه" in text:
        return "MONTHLY_SALES"

    return "GPT_GENERAL"
