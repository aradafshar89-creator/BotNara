from app.api.forecast import router as forecast_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.upload import router as upload_router
from app.api.analytics import router as analytics_router
from app.api.chat import router as chat_router
from app.api.advisor import router as advisor_router

app = FastAPI(
    title="BotNara API",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Upload
app.include_router(
    upload_router,
    prefix="/api"
)

# Analytics
app.include_router(
    analytics_router,
    prefix="/api/analytics"
)

# Chat AI
app.include_router(
    chat_router,
    prefix="/api"
)

# Business Advisor
app.include_router(
    advisor_router,
    prefix="/api"
)

app.include_router(
    forecast_router,
    prefix="/api"
)

@app.get("/")
def root():
    return {
        "message": "BotNara API Running",
        "version": "0.1.0"
    }
