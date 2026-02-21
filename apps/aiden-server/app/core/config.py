from typing import Any, Optional

from pydantic import PostgresDsn, ValidationInfo, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "AIDEN Server"
    API_V1_STR: str = "/api/v1"

    POSTGRES_SERVER: str = "localhost"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "password"
    POSTGRES_DB: str = "aiden"

    # Can be sqlite or postgres
    DATABASE_URL: Optional[str] = None

    @field_validator("DATABASE_URL", mode="before")
    @classmethod
    def assemble_db_connection(cls, v: Optional[str], info: ValidationInfo) -> Any:
        if isinstance(v, str):
            return v

        # Fallback to postgres if not provided
        return str(PostgresDsn.build(
            scheme="postgresql+asyncpg",
            username=info.data.get("POSTGRES_USER"),
            password=info.data.get("POSTGRES_PASSWORD"),
            host=info.data.get("POSTGRES_SERVER"),
            path=info.data.get("POSTGRES_DB") or "",
        ))

    REDIS_URL: str = "redis://localhost:6379/0"

    # AI Services
    ANTHROPIC_API_KEY: Optional[str] = None
    OPENAI_API_KEY: Optional[str] = None

    # Data Providers (Optional for now as we mock them)
    APOLLO_API_KEY: Optional[str] = None
    PROXYCURL_API_KEY: Optional[str] = None
    BUILTWITH_API_KEY: Optional[str] = None
    NEWS_API_KEY: Optional[str] = None

    # Error Tracking
    SENTRY_DSN: Optional[str] = None
    ENVIRONMENT: str = "local"  # local, staging, production

    model_config = SettingsConfigDict(
        case_sensitive=True,
        env_file=".env",
        extra="ignore"
    )

settings = Settings()
