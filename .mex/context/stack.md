---
name: stack
description: Runtime and libraries used by the single-file Gemini chatbot.
triggers:
  - "library"
  - "package"
  - "dependency"
  - "technology"
edges:
  - target: context/architecture.md
    condition: when a technology detail changes the request flow
  - target: context/setup.md
    condition: when installing or configuring the runtime
  - target: context/conventions.md
    condition: when using these libraries in app.py
  - target: patterns/configure-gemini.md
    condition: when changing the Gemini, LangChain, dotenv, or Gradio boundary
grounds_to: []
last_updated: 2026-09-28
---

# Stack

## Core Technologies
- **Python** — runtime and application language; exact version is `[TO DETERMINE]`.
- **Gradio** — browser UI framework, used through `ChatInterface`.
- **LangChain** — message and model integration layer.
- **Google Gemini** — remote LLM provider, configured as `gemini-3.5-flash-lite` by default and overrideable with `GEMINI_MODEL`.

## Key Libraries
- **`gradio`** — creates the conversational UI and calls the callback.
- **`python-dotenv`** — loads `.env` values into the process.
- **`langchain-google-genai`** — supplies `ChatGoogleGenerativeAI`.
- **`langchain-core`** — supplies `HumanMessage` and the message representation passed to the model.

## What We Deliberately Do NOT Use
- No alternative web framework is present; do not introduce a second UI server without an explicit design decision.
- No direct Google SDK call is present; model invocation goes through `ChatGoogleGenerativeAI`.
- No database, ORM, test framework, linter, or build tool is declared by the project brief.

## Version Constraints
The exact Python and package versions are `[TO DETERMINE]`; no manifest or lockfile is identified by the project brief.
