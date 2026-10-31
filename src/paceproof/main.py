"""FastAPI application factory."""

from pathlib import Path

import sentry_sdk
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.trustedhost import TrustedHostMiddleware

from . import __version__
from .config import Settings, get_settings
from .i18n import _
from .security import SameOriginMiddleware, SecurityHeadersMiddleware

HERE = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=HERE / "templates")
templates.env.globals["_"] = _


def create_app(settings: Settings | None = None) -> FastAPI:
    settings = settings or get_settings()

    if settings.sentry_dsn:
        sentry_sdk.init(
            dsn=settings.sentry_dsn,
            environment=settings.environment,
            release=f"paceproof@{__version__}",
            traces_sample_rate=settings.sentry_traces_sample_rate,
            send_default_pii=False,
        )

    app = FastAPI(title="PaceProof", version=__version__, docs_url=None, redoc_url=None, openapi_url=None)
    app.state.settings = settings

    # Order matters: the last added middleware runs first.
    app.add_middleware(SecurityHeadersMiddleware, hsts=settings.is_production)
    app.add_middleware(SameOriginMiddleware)
    app.add_middleware(TrustedHostMiddleware, allowed_hosts=settings.allowed_hosts)

    app.mount("/static", StaticFiles(directory=HERE / "static"), name="static")

    @app.get("/healthz", include_in_schema=False)
    def healthz() -> dict[str, str]:
        return {"status": "ok", "version": __version__}

    @app.get("/", response_class=HTMLResponse)
    def landing(request: Request) -> HTMLResponse:
        return templates.TemplateResponse(request, "landing.html", {"invite_only": settings.invite_only})

    return app


app = create_app()
