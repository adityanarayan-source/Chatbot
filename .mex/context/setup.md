---
name: setup
description: Local prerequisites, configuration, and launch procedure for the chatbot.
triggers:
  - "setup"
  - "install"
  - "environment"
  - "how do I run"
edges:
  - target: context/stack.md
    condition: when package or version details are needed
  - target: context/architecture.md
    condition: when diagnosing startup or request flow
  - target: patterns/debug-startup.md
    condition: when launch or API configuration fails
grounds_to: []
last_updated: 2026-09-28
---

# Setup

## Prerequisites
- Python; exact supported version is `[TO DETERMINE]`.
- A Google API key available as `GOOGLE_API_KEY`.
- The packages imported by `app.py`: `gradio`, `python-dotenv`, `langchain-google-genai`, and `langchain-core`.

## First-time Setup
1. Create and activate a Python virtual environment using the local Python installation.
2. Install the four packages imported by `app.py`; the repository does not declare a manifest in the supplied brief.
3. Provide `GOOGLE_API_KEY` through the environment or a local `.env` file.
4. Run `python app.py` and open the Gradio URL printed by the process.

## Environment Variables
- `GOOGLE_API_KEY` (required) — credential passed to `ChatGoogleGenerativeAI`.

## Common Commands
- `python app.py` — starts the Gradio interface.
- `python -m py_compile app.py` — checks Python syntax without launching the UI.
- `[TO DETERMINE]` — test command; no test runner is declared.
- `[TO DETERMINE]` — lint command; no linter is declared.

## Common Issues
**Missing model credential:** confirm `GOOGLE_API_KEY` is available before starting `app.py`.

**Dependency import failure:** install the packages corresponding to the imports in `app.py`; no lockfile or manifest is identified.
