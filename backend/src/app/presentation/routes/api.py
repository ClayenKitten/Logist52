
from fastapi import APIRouter

from app.presentation.routes.product import router as product_router
from app.presentation.routes.purchase import router as purchase_router
from app.presentation.routes.role import router as role_router
from app.presentation.routes.supply import router as supply_router
from app.presentation.routes.user import router as user_router

api_router = APIRouter(prefix="/api")

api_router.include_router(user_router, tags=["Пользователь"])
api_router.include_router(role_router, tags=['Роли'])
api_router.include_router(purchase_router, tags=["Покупки"])
api_router.include_router(supply_router, tags=['Поставки'])
api_router.include_router(product_router, tags=['Продукты'])
