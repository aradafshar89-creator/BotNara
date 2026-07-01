from app.api.analytics import router as analytics_router
from app.api.chat import router as chat_router
from fastapi import FastAPI
from app.api.upload import router as upload_router

app = FastAPI(title="BotNara API")

app.include_router(upload_router, prefix="/api")
app.include_router(
    analytics_router,
    prefix="/api/analytics"
)

app.include_router(
    chat_router,
    prefix="/api"
)
@app.get("/")
def root():
    return {
        "message": "BotNara API Running",
        "version": "0.1.0"
    }
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # برای تست
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
