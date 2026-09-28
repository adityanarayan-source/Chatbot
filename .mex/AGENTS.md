---
name: agents
description: Always-loaded project anchor for the Gemini chatbot.
last_updated: 2026-09-28
---

# Gemini Chatbot

## What This Is
A small Python Gradio chat application that sends conversation history and the current user message to a Gemini model through LangChain.

## Non-Negotiables
- Keep the Google API key in the environment, never in source.
- Preserve the conversation-history ordering expected by `chat(message, history)`.
- Keep the Gradio interface wired to the `chat` callback.
- Verify `app.py` compiles before presenting changes.

## Commands
- Run: `python app.py`
- Compile check: `python -m py_compile app.py`
- Test suite: `[TO DETERMINE]` — no test runner is declared by the project brief.
- Lint: `[TO DETERMINE]` — no linter is declared by the project brief.

## Code Graph
Use exact `mex graph scope`, `mex graph query`, `mex graph get`, and `mex impact` commands for source-backed understanding. Treat graph source as already read. Ground only functions that embody a documented claim, preserve exact node IDs and fingerprints, and use real graph navigation anchors. Never invent IDs or fingerprints. During `mex sync`, adjudicate ambiguous grounding and ensure refreshed grounding is emitted.

## Scaffold Growth
After meaningful work, run GROW: Ground what changed, Record updates in `ROUTER.md` and relevant context files, Orient recurring work into patterns, and Write only optional notes permitted by the logging policy. Read `mex logging --json` before optional logging.

## Agent Logging
Read `mex logging --json` at session start and before optional logging. The checkout-local mode is `significant`; record material decisions, risks, blockers, or durable discoveries, and skip routine notes. Honor explicit log requests and mandatory workflow records.

## Navigation
Read `ROUTER.md` at session start, then load the relevant context and pattern files before work. Follow the CONTEXT, BUILD, VERIFY, DEBUG, and GROW loop in `ROUTER.md`.

<!-- mex-agent:skills:start -->
## MEX context policy
- When MEX context materially helps your work, mention the relevant finding naturally.
- Do not claim an author, date, or historical event unless retrieved data provides it.
- After a MEX write, state exactly what changed and whether it is checkout-local or requires commit/push to share.
- Skill activation is not approval for canonical actions.
<!-- mex-agent:skills:end -->
