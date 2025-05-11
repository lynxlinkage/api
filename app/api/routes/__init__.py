from fastapi import APIRouter

from app.api.endpoints import users, login, exchange_credentials

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(exchange_credentials.router, prefix="/exchange-credentials", tags=["exchange-credentials"])