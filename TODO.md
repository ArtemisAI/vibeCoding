# TODO – Next actionable tasks

This list is intentionally short.  As soon as an item is completed, open a PR, check it off, and **add the next step**.

- [x] Configure a minimal Continuous Integration workflow that:
  - Installs the project (editable mode).
  - Runs `pytest`.
  - Fails on linter errors (`black --check` and `flake8`).

- [x] Implement the logger utility in `src/python/vibecoding/logging.py` with tests.

- [x] Document the logger in `docs/` and update `ROADMAP.md` once merged.
- [ ] Implement a typed config loader in `src/python/vibecoding/config.py` with tests.
- [ ] Expose a simple HTTP server (FastAPI) that replies with build info.
