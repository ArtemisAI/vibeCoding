# Manual Tasks and Environment Requirements

This file collects steps that **cannot be automated** and therefore require a human to perform them. AI agents should append a short entry whenever they discover such a requirement.

## When to add an entry

- Secret provisioning or credential setup that cannot be stored in the repository.
- Operating system or hardware changes that must be executed outside of Docker.
- Any manual verification or process that a human must complete before CI/CD can succeed.

## Format

Use a bullet list with a brief description and the date. Example:

- 2023-01-01: Obtain API key for service X and place it in `.env`.
- 2023-01-02: Run `docker compose build` after installing new system packages.

Keep entries concise and update them when the requirement is no longer relevant.
