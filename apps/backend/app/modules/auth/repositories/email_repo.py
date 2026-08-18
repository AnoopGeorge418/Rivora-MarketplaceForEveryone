from typing import final

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.auth.models.user_model import Users


@final
class EmailRepository:

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def check_user_by_email(self, email: str):
        """Checks if user in db or not using email"""
        
        user = select(Users).where(Users.email == email)
        result = await self.session.execute(user)

        return result.scalar_one_or_none()
