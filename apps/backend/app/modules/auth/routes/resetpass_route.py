# routes/resetpass_route.py
from fastapi import APIRouter

resetpass_router = APIRouter(prefix="/password", tags=["Password Reset"])


@resetpass_router.post("/forgot")
async def forgot_password(): ...


@resetpass_router.post("/reset")
async def reset_password(): ...
