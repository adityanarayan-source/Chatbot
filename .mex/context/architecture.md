---
name: architecture
description: How the chatbot loads configuration, builds messages, calls Gemini, and exposes the UI.
triggers:
  - "architecture"
  - "system design"
  - "request flow"
  - "integration"
edges:
  - target: context/stack.md
    condition: when library and runtime details are needed
  - target: context/setup.md
    condition: when reproducing the local launch flow
  - target: patterns/debug-startup.md
    condition: when the startup or model boundary fails
grounds_to: []
last_updated: 2026-09-28
---

# Architecture

## System Overview
`app.py` loads environment variables at import time.
It constructs a `ChatGoogleGenerativeAI` client for `gemini-3.8-flash`.
Gradio calls [`chat()`](mex://function:1a1a0b31a2e453a40b034788c9d09f84) with the current message and prior pairs.
The callback converts each prior pair into ordered LangChain `HumanMessage` objects.
It appends the current user message and invokes the Gemini client.
The returned model content becomes the Gradio response.
Running `app.py` launches the configured `ChatInterface`.

## Key Components
- **Environment loading** — `python-dotenv` populates process configuration before model initialization.
- **Gemini model client** — `ChatGoogleGenerativeAI` is configured with `GOOGLE_API_KEY`, the Gemini model name, and temperature `0.7`.
- **Chat callback** — [`chat()`](mex://function:1a1a0b31a2e453a40b034788c9d09f84) translates history and returns `response.content`.
- **Gradio interface** — `ChatInterface` owns the textbox and delegates each turn to the callback.

## External Dependencies
- **Google Gemini** — remote model provider invoked through LangChain; requires `GOOGLE_API_KEY`.
- **Gradio** — local web UI and callback orchestration.
- **LangChain Google GenAI integration** — model adapter used to invoke Gemini.
- **python-dotenv** — reads local environment configuration.

## What Does NOT Exist Here
- No persistence layer or database is present in the indexed project.
- No separate backend API, worker, or deployment configuration is present.
- No automated test, lint, or build pipeline is declared by the project brief.
