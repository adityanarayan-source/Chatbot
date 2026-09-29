---
name: router
description: Session bootstrap and navigation hub for the Gemini chatbot scaffold.
triggers:
  - "session bootstrap"
  - "route context"
edges:
  - target: context/architecture.md
    condition: when understanding the request-to-model-to-UI flow
  - target: context/stack.md
    condition: when changing Python, Gradio, LangChain, or Gemini usage
  - target: context/setup.md
    condition: when installing dependencies or running the app
  - target: patterns/INDEX.md
    condition: at the start of any implementation or debugging task
last_updated: 2026-09-28
---

# Session Bootstrap

Read `.mex/AGENTS.md`, then this file, before project work. Load the context and pattern files selected by the routing table.

## Current Project State
**Working:**
- `app.py` initializes a Gemini chat model and exposes a Gradio `ChatInterface`.
- Conversation history is stored in SQLite per Gradio session and converted into role-aware LangChain messages before model invocation.
- Gradio 6 OpenAI-style history dictionaries and legacy tuple history are both supported.

**Not yet built:**
- Automated tests, linting, and build tooling are not declared.
- Additional application modules, persistence, and deployment configuration are not present in the indexed project.

**Known issues:**
- The required `GOOGLE_API_KEY` environment contract is not validated explicitly before model construction.
- The project brief does not identify a dependency manifest or reproducible installation command.
- A stale local proxy configuration (`127.0.0.1:9`) can block Gemini requests; launch the app without those proxy variables when that proxy is unavailable.

## Routing Table
| Task type | Load |
|-----------|------|
| Understanding the request and response flow | `context/architecture.md` |
| Working with Python, Gradio, LangChain, or Gemini | `context/stack.md` |
| Writing or reviewing code | `context/conventions.md` |
| Understanding implementation choices | `context/decisions.md` |
| Installing or running locally | `context/setup.md` |
| Any specific task | `patterns/INDEX.md` |

## Behavioural Contract
1. **CONTEXT** — Load the relevant context file and check `patterns/INDEX.md`.
2. **BUILD** — Make the smallest evidence-backed change.
3. **VERIFY** — Load `context/conventions.md` and enumerate its checklist.
4. **DEBUG** — If verification fails, follow the relevant debug pattern and retry.
5. **GROW** — Ground changes, record current state, orient recurring work into patterns, and write only policy-allowed notes.

## Code Graph
Use `mex graph scope "<task>" --fingerprint` for broad discovery, exact `mex graph query` for known symbols, `mex graph get <id> --detail source` for expansion, and `mex impact <symbol|file>` before editing. Read broad, ground tight. Never invent IDs or fingerprints.
