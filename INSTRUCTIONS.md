# Instructions for AI Agents and Human Contributors

This file is **pulled automatically** by autonomous agents (for example, the OpenAI Codex CLI) every time they start a new task.  Keep it short, explicit and up-to-date.

## 1. Workflow

1. Pick the **next unchecked item** in `TODO.md`.
2. Create a *small* pull-request that focuses **only on that item**.
3. Ensure `pytest` passes locally and in CI.
4. Update the documentation:
   * Mark the TODO item as done.
   * If the change impacts the big picture, reflect it in `docs/ROADMAP.md`.
   * Add a short entry in `changelog/` describing *what* and *why* you changed.
5. Request review or merge.

## 2. Coding conventions

* Default language: **Python 3.11**.
* Follow **PEP 8** plus `black` formatting (line-length = 88).
* Add **type hints** for all new public functions/classes.
* Every non-trivial function must have meaningful **doc-strings**.
* Use **pytest** for tests; put them under `tests/` mirroring the source tree.
* Never commit secrets.  Reference them via environment variables and document every variable in `.env.example`.
* `pre-commit` runs `detect-secrets` to prevent leaks.  If you add new allowed values, update `.secrets.baseline` with `detect-secrets scan > .secrets.baseline` and commit it.

## 3. Repository layout (high-level)

```
├── docs/                 # project-level documentation
│   ├── ROADMAP.md        # strategic plan, updated regularly
│   └── ...
├── src/                  # Python source code (packages live here)
├── tests/                # pytest test-suite
├── changelog/            # one file per PR describing the change in first-person
├── .env.example          # example env vars (never commit real credentials!)
├── docker-compose.yml    # reproducible dev environment
└── ...
```

## 4. Logging & Debugging

* Application logs go to the `logs/` directory (ignored in `.gitignore`).
* When you catch an exception that you *cannot* recover from, log it and **re-raise** so tests/CI fail loudly.

## 5. Commit messages

Use the following template for commit messages and for the `changelog/` entry:

```
<area>: <imperative summary>

Why:
    <optional context explaining the motivation>

How:
    <optional brief of the implementation>
```

## 6. When in doubt

If a guideline is missing or unclear, open an issue, propose an update to this file, or ask in the discussion board.  **Documentation is code** – keep it alive.
