from typing import final

from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.auth.repositories.email_repo import EmailRepository
from app.modules.auth.schemas.signup_auth_schema import SignupRequestSchema


@final
class EmailService:
    """Performs business logics on Email Authentication"""

    def __init__(self, session: AsyncSession):
        self.session = session
        self.repo = EmailRepository(session)

    async def get_user_by_email(self, email: str):
        """Returns True if user is registered in db else returns user not found"""
        if not email:
            raise ValueError("Please enter a valid email address!")

        result = await self.repo.check_user_by_email(email=email)
        if result:
            ...
