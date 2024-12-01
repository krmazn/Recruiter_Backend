from fastapi import APIRouter
from .endpoints.user_request import router
#APIRouter.include_router(router)
api_router = APIRouter()
api_router.include_router(router)