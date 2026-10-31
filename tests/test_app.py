from fastapi.testclient import TestClient

from paceproof import __version__
from paceproof.config import Settings
from paceproof.main import create_app


def test_healthz(client: TestClient) -> None:
    resp = client.get("/healthz")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok", "version": __version__}


def test_landing_shows_invite_only_badge(client: TestClient) -> None:
    resp = client.get("/")
    assert resp.status_code == 200
    assert "Private beta" in resp.text


def test_security_headers(client: TestClient) -> None:
    resp = client.get("/")
    assert resp.headers["X-Content-Type-Options"] == "nosniff"
    assert resp.headers["X-Frame-Options"] == "DENY"
    assert "Strict-Transport-Security" not in resp.headers


def test_hsts_in_production() -> None:
    settings = Settings(_env_file=None, environment="production", allowed_hosts=["testserver"])
    resp = TestClient(create_app(settings)).get("/healthz")
    assert resp.headers["Strict-Transport-Security"].startswith("max-age=")


def test_unknown_host_rejected(client: TestClient) -> None:
    assert client.get("/", headers={"host": "evil.example"}).status_code == 400


def test_cross_origin_post_blocked(client: TestClient) -> None:
    resp = client.post("/", headers={"origin": "https://evil.example"})
    assert resp.status_code == 403


def test_allowed_hosts_from_csv_env(monkeypatch) -> None:
    monkeypatch.setenv("ALLOWED_HOSTS", "a.example, b.example")
    assert Settings(_env_file=None).allowed_hosts == ["a.example", "b.example"]
