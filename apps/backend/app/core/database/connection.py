from app.core.config.settings import APP_SETTINGS
from sqlalchemy.ext.asyncio import create_async_engine

connect_args = {}

if APP_SETTINGS.APP_ENVIRONMENT == "production":
    connect_args["ssl"] = "require"

async_engine = create_async_engine(
    url=APP_SETTINGS.switch_db_using_env,
    echo=APP_SETTINGS.DATABASE_ECHO_LOGS,
    connect_args=connect_args,
    future=True,
)
