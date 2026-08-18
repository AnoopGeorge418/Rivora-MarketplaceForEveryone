from fastapi import APIRouter, HTTPException
from starlette import status

from app.core.database.dependency import DBSession
from app.modules.auth.schemas.signup_auth_schema import (
    SignupRequestSchema,
    SignupResponseSchema,
)
from app.modules.auth.services.email_service import EmailService

signup_router = APIRouter(prefix="/signup", tags=["Signup"])


@signup_router.post("/", response_model=SignupResponseSchema, status_code=status.HTTP_200_OK)
async def signup(payload: SignupRequestSchema, session: DBSession):
    service = EmailService(session)
    existing_user = await service.get_user_by_email(email=payload.email)

    if existing_user is not None:
       raise HTTPException(
           status_code=status.HTTP_409_CONFLICT,
           detail="An account with this email already exists."
       ) 
