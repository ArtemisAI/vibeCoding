# Contributing to VibeCoding

Thank you for considering contributing!  Whether you are a human developer or an autonomous agent, these guidelines will help you get your changes merged smoothly.

## Development environment

1. Copy `.env.example` to `.env` and adjust values as necessary.
2. `docker compose up -d` to start dependencies.
3. `docker compose exec app bash` drops you inside the running container with all dev dependencies installed.

## Pre-commit checks

We use `pre-commit` to run `black`, `flake8` and other hooks.  Set it up locally:

```bash
pip install pre-commit
pre-commit install
```

Checks also run in CI.  A failing hook will block the merge.

## Opening a pull-request

1. Ensure `pytest` passes: `pytest -q`.
2. Document your change:
   * Update `TODO.md` and `docs/ROADMAP.md` if applicable.
   * Add a file in `changelog/` describing the change in first person (`I changed …`).
3. Use the pull-request template (GitHub will suggest it automatically).

## Code of Conduct

We follow the [Contributor Covenant](https://www.contributor-covenant.org/version/2/0/code_of_conduct/).  Be respectful.
