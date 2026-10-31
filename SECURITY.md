# Security Policy

## Reporting a vulnerability

Please **do not open a public issue** for security problems.

Report vulnerabilities privately via GitHub's
[private vulnerability reporting](https://github.com/mikonoid/paceproof/security/advisories/new).
We aim to acknowledge reports within 3 working days.

## Scope

- The PaceProof web application in this repository.
- Out of scope: third-party services (Fly.io, Neon, Google, Anthropic, Resend, Sentry, Intervals.icu).

## Data handling principles

- Uploaded activity files (`.fit`, `.gpx`, `.tcx`) are processed in memory and never stored.
- Secrets live only in the hosting platform's secret store, never in the repository.
