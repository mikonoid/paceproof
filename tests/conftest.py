import pytest
from fastapi.testclient import TestClient

from paceproof.config import Settings
from paceproof.main import create_app


@pytest.fixture
def settings() -> Settings:
    return Settings(_env_file=None, environment="test", allowed_hosts=["testserver"])


@pytest.fixture
def client(settings: Settings) -> TestClient:
    return TestClient(create_app(settings))
