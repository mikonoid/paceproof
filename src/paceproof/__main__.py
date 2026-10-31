"""Run the app: `python -m paceproof` (or the `paceproof` console script)."""

import uvicorn

from .config import get_settings


def main() -> None:
    settings = get_settings()
    uvicorn.run(
        "paceproof.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.environment == "development",
        proxy_headers=True,
        forwarded_allow_ips="*" if settings.is_production else "127.0.0.1",
    )


if __name__ == "__main__":
    main()
