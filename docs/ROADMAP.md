# VibeCoding – Roadmap

This roadmap is intentionally *high-level*.  Each milestone will be broken down into actionable tasks in `TODO.md`.

## Milestone 1 – Repository bootstrap (you are here)

Goal: Establish the minimal but complete scaffolding that enables productive collaboration and continuous quality control.

Checklist:

* [x] Documentation skeleton (`README`, `INSTRUCTIONS`, `ROADMAP`).
* [x] Development tooling (`docker-compose`, `.env.example`).
* [x] Test scaffolding (`pytest`, a sample test to keep CI green).
* [ ] Continuous Integration (GitHub Actions or similar).

## Milestone 2 – Core package `vibecoding`

Goal: Create an installable Python package that offers helper utilities common to all future services (e.g. logging, config loading, health-check endpoint).

Tasks (non-exhaustive):

1. Implement a structured logger wrapper.
2. Provide a typed config loader that reads from env vars.
3. Expose a simple HTTP server (FastAPI) that replies with build info.

## Milestone 3 – AI Agent integration

Goal: Introduce the first autonomous coding agent that can read the repository, run tests, and open PRs.

High-level tasks:

1. Research and pick an agent framework (AutoGPT, CrewAI, custom?).
2. Dockerize the agent so it can run in isolation.
3. Define permission boundaries (allowed commands, timeouts, etc.).

## Milestone 4 – Feature projects

Once the core is stable, we will start separate micro-projects (e.g. a CLI tool, a web dashboard, automation scripts).  Each will live in its own directory under `src/` and will have its own milestone list.

---

Last updated: <!-- PLACEHOLDER:CI_DATE -->
