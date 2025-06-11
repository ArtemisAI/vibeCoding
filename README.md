# VibeCoding

VibeCoding is a **developer-first** workspace that leverages AI agents (like the OpenAI Codex CLI you are using right now) to design, build and maintain software projects **one focused task at a time**.

This repository is the **blank canvas** on top of which we will iteratively build applications, scripts and services.  It already contains guard-rails, documentation and tests that enable humans and AI contributors to collaborate safely and efficiently.

## Why does this repo look “empty”?

Instead of shipping a monolithic boiler-plate, VibeCoding starts with only the scaffolding that ensures quality and order:

* A clear, up-to-date **ROADMAP** that explains *where* we are heading.
* A living **TODO** list that breaks the roadmap into small, bite-sized tasks.
* **Instructions** for AI agents so every autonomous contributor shares the same ground rules.
* A reproducible **docker-compose** environment so anybody can start hacking with a single command.
* Continuous **tests** – even at this early stage – to keep us honest while we evolve the code-base.
* Source code is organized by language under `src/<language>/`.

Everything else will be generated incrementally as we advance through the roadmap.

## Quick start

```bash
# Clone and enter the repo
git clone <your-fork-url>
cd vibeCoding

# Spin up the dev stack (adds a dedicated network, volumes, etc.)
docker compose up -d

# Run the test-suite
docker compose exec app pytest -q
```

## Contributing

Pull-requests are welcome!  Please read `docs/CONTRIBUTING.md` for guidelines.

If you are an **AI agent** (👋), read `INSTRUCTIONS.md` first – it describes the communication protocol, coding conventions and the structure you can expect in this repository.

## Project status

The project is in **bootstrap** stage.  The immediate goals are listed in `TODO.md` and the higher-level plan sits in `docs/ROADMAP.md`.

---

Made with care by the VibeCoding community.
