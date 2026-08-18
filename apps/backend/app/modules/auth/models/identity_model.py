import datetime
import uuid

from sqlalchemy import (
    UUID,
    Boolean,
    DateTime,
    Enum,
    ForeignKey,
    String,
    UniqueConstraint,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import TYPE_CHECKING

from app.core.database.base import Base
from app.modules.auth.enums.auth_provider_enum import AuthProvidersEnum

# handles circular import
if TYPE_CHECKING:
    from app.modules.auth.models.user_model import Users


class Identity(Base):
    __tablename__: str = "identities"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), default=uuid.uuid4, primary_key=True
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id"), index=True, nullable=False
    )

    provider: Mapped[AuthProvidersEnum] = mapped_column(
        Enum(AuthProvidersEnum), nullable=False
    )
    provider_user_id: Mapped[str] = mapped_column(String, nullable=False)

    hashed_password: Mapped[str | None] = mapped_column(String, nullable=True)
    is_verified: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        insert_default=func.now(),
        server_default=func.now(),
        nullable=False,
    )
    last_used_at: Mapped[datetime.datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )

    # uniqueness - restricts - multiple users login using same google account
    __table_args__ = (
        UniqueConstraint("provider", "provider_user_id", name="uq_provider_identity"),
    )

    # relationship
    user: Mapped["Users"] = relationship(back_populates="identities")
