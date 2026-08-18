import datetime
import uuid

from sqlalchemy import UUID, Boolean, DateTime, Enum, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import TYPE_CHECKING

from app.core.database.base import Base
from app.modules.auth.enums.auth_roles_enum import AuthRolesEnum
from app.modules.auth.enums.onboarding_enum import OnboardingStatusEnum

# handles circular import
if TYPE_CHECKING:
    from app.modules.auth.models.identity_model import Identity
    from app.modules.auth.models.session_model import Session


class Users(Base):
    __tablename__: str = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), default=uuid.uuid4, primary_key=True
    )

    username: Mapped[str] = mapped_column(
        String, unique=True, index=True, nullable=False
    )
    firstname: Mapped[str] = mapped_column(String, nullable=False)
    lastname: Mapped[str] = mapped_column(String, nullable=False)

    email: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    role: Mapped[AuthRolesEnum] = mapped_column(
        Enum(AuthRolesEnum), index=True, nullable=False, default=AuthRolesEnum.USER
    )

    onboarding_status: Mapped[OnboardingStatusEnum] = mapped_column(
        Enum(OnboardingStatusEnum),
        nullable=False,
        default=OnboardingStatusEnum.PENDING_VERIFICATION,
    )
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    last_logged_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        insert_default=func.now(),
        server_default=func.now(),
        nullable=False,
    )
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        insert_default=func.now(),
        server_default=func.now(),
        nullable=False,
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        insert_default=func.now(),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    # relationship
    identities: Mapped[list["Identity"]] = relationship(back_populates="user")
    sessions: Mapped[list["Session"]] = relationship(back_populates="user")
