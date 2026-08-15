from app.core.database.base import Base


class Session(Base):
    __tablename__: str = "session"
