from typing import final

from sqlalchemy.ext.asyncio import AsyncSession


@final
class EmailRepository:

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def check_user_by_email(self, email: str):
        """Checks if user in db or not using email"""

        ...
