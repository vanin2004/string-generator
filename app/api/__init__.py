from fastapi import APIRouter
from app.api.random_string import router as random_string_router

router = APIRouter(prefix="/api")

router.include_router(random_string_router)