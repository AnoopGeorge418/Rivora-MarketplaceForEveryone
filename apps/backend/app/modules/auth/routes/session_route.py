# routes/session_route.py
from fastapi import APIRouter

session_router = APIRouter(prefix="/session", tags=["Session"])


@session_router.post("/refresh")
async def refresh_token(): ...


@session_router.post("/logout")
async def logout(): ...
