from app.services.context_service import build_company_context

from app.services.openai_service import ask_gpt
from app.services.openai_service import ask_gpt


def chat_with_database(question):

    context = build_company_context()


    prompt = f"""
تو دستیار مدیریتی BotNara هستی.

اطلاعات شرکت:

Company Data:

{context}

سوال مدیر:

{question}

فقط بر اساس اطلاعات بالا جواب بده.

اگر اطلاعات کافی نبود بگو:
"اطلاعات کافی در دیتابیس وجود ندارد."
"""

    return ask_gpt(prompt)
