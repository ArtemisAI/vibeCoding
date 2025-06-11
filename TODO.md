# TODO – Next actionable tasks

This list is intentionally short.  As soon as an item is completed, open a PR, check it off, and **add the next step**.

- [x] Configure a minimal Continuous Integration workflow that:
  - Installs the project (editable mode).
  - Runs `pytest`.
  - Fails on linter errors (`black --check` and `flake8`).

- [ ] Implement the logger utility in `src/vibecoding/logging.py` with tests.

- [ ] Document the logger in `docs/` and update `ROADMAP.md` once merged.
- [ ] Implement a typed config loader in `src/vibecoding/config.py` with tests.
