# Architecture Overview

This document sketches the intended high-level design of VibeCoding.
It will evolve as modules are added.

## Core package

All common utilities live in the `vibecoding` Python package. It holds
logging, configuration and other helpers that future services can import.

## Feature modules

Each service or tool will reside in its own directory under `src/`
or directly under the repository root. Modules may be written in
other languages when appropriate. Regardless of language, every module
must expose a minimal API so other parts of the system can interact
with it via clearly defined interfaces.

## Cross-language interaction

Language-specific modules communicate through HTTP APIs, command-line
interfaces or message queues. For example, a Python service could call a
Rust CLI tool as a subprocess, or send requests to a FastAPI endpoint.
The architecture favors loose coupling so components remain replaceable.

Updates to this document should accompany any structural change to the
code base.
