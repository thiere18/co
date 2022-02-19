from fastapi import APIRouter
from app.api_v1.routers import auth,user,role
router = APIRouter()

router.include_router(auth.router)
router.include_router(user.router)
router.include_router(role.router)