# PaceProof

**Understand every run. Prepare for every race.**

PaceProof turns your activity files into clear, explainable insights:

- **Drop your FIT** — upload a `.fit`, `.gpx` or `.tcx` file and get splits, heart-rate zones, aerobic
  decoupling, pace stability and best efforts, plus short AI feedback. Your original file is never stored.
- **Race Prep Planner** *(coming next)* — adaptive training plans for 5K to marathon that explain every
  workout, adapt every week and sync to your calendar or watch.

> 🚧 Private beta — access is invite-only.

## Tech stack

Python · FastAPI · Jinja2 + HTMX · PostgreSQL · Docker · Fly.io

## Running locally

```bash
python3 -m venv .venv
.venv/bin/pip install -e ".[dev]"
cp .env.example .env
.venv/bin/python -m paceproof
```

Open <http://localhost:8000>. Health check: `/healthz`.

With Docker (app + Postgres):

```bash
docker compose up --build
```

## Tests & linting

```bash
.venv/bin/pytest
.venv/bin/ruff check . && .venv/bin/ruff format --check .
```

## Deployment

Pushes to `main` run CI and, once the `FLY_API_TOKEN` secret is configured, deploy to Fly.io
(see [`fly.toml`](fly.toml) and [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml)).

## Contributing & security

See [CONTRIBUTING.md](CONTRIBUTING.md) (commits must be signed off — DCO) and [SECURITY.md](SECURITY.md).

## License

[Functional Source License, Version 1.1, ALv2 Future License](LICENSE.md) (FSL-1.1-ALv2).
You may use, modify and self-host PaceProof for any purpose other than offering a competing commercial
service. Each version becomes available under the Apache License 2.0 two years after its release.

PaceProof is not affiliated with Garmin, Strava, COROS, Suunto, Polar or Intervals.icu.
Training information is for educational purposes only and is not medical advice.