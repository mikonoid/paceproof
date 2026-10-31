"""Application settings, loaded from environment variables (and `.env` in development)."""

from functools import lru_cache
from typing import Annotated, Literal

from pydantic import field_validator
from pydantic_settings import BaseSettings, NoDecode, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    environment: Literal["development", "test", "production"] = "development"
    host: str = "127.0.0.1"
    port: int = 8000
    base_url: str = "http://localhost:8000"

    # Comma-separated in env, e.g. ALLOWED_HOSTS=paceproof.fly.dev,paceproof.app
    allowed_hosts: Annotated[list[str], NoDecode] = ["localhost", "127.0.0.1"]
    invite_only: bool = True

    sentry_dsn: str = ""
    sentry_traces_sample_rate: float = 0.0

    @field_validator("allowed_hosts", mode="before")
    @classmethod
    def _split_csv(cls, value: object) -> object:
        if isinstance(value, str):
            return [item.strip() for item in value.split(",") if item.strip()]
        return value

    @property
    def is_production(self) -> bool:
        return self.environment == "production"


@lru_cache
def get_settings() -> Settings:
    return Settings()
