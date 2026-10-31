# Contributing

Thanks for your interest in PaceProof! The project is in a private beta, so the scope is still moving quickly —
please open an issue to discuss larger changes before sending a pull request.

## Development setup

```bash
python3 -m venv .venv
.venv/bin/pip install -e ".[dev]"
cp .env.example .env
.venv/bin/python -m paceproof          # http://localhost:8000
.venv/bin/pytest
.venv/bin/ruff check . && .venv/bin/ruff format --check .
```

Or with Docker: `docker compose up --build`.

## Developer Certificate of Origin (DCO)

All commits must be signed off to certify you wrote the code or have the right to submit it under the
project's license ([DCO 1.1](https://developercertificate.org/)):

```bash
git commit -s -m "Your message"
```

This adds a `Signed-off-by: Your Name <you@example.com>` line to the commit message.

## License

By contributing, you agree that your contributions are licensed under the project's
[Functional Source License, Version 1.1, ALv2 Future License](LICENSE.md).

## Test data

Only commit activity files you recorded yourself or generated synthetically — never other people's data.
