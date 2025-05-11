from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import api_router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="0.1.0",
    description="Simple PMS API"
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Include API router with the API_V1_STR prefix
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/health", tags=["health"])
async def health_check():
    return {"status": "healthy", "message": "Service is up and running"}