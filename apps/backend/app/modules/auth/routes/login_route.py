# routes/login_route.py
from fastapi import APIRouter

from app.modules.auth.schemas.login_auth_schema import LoginRequestSchema, TokenResponse

login_router = APIRouter(prefix="/login", tags=["Login"])


@login_router.post("/", response_model=TokenResponse)
async def login(payload: LoginRequestSchema): ...
