from fastapi import APIRouter

from app.core.database.dependency import DBSession
from app.modules.auth.schemas.signup_auth_schema import (
    SignupRequestSchema,
    SignupResponseSchema,
)
from app.modules.auth.services.email_service import EmailService

signup_router = APIRouter(prefix="/signup", tags=["Signup"])


@signup_router.post("/", response_model=SignupResponseSchema)
async def signup(payload: SignupRequestSchema, session: DBSession):
    service = EmailService(session)
    response = await service.get_user_by_email(email=payload.email)

    return response
