from fastapi import APIRouter
from endpoints.user_request import router
APIRouter.include_router(router)
