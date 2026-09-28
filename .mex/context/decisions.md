---
name: decisions
description: Observable implementation choices in the single-file chatbot and unresolved rationale.
triggers:
  - "why do we"
  - "decision"
  - "alternative"
edges:
  - target: context/architecture.md
    condition: when a choice affects system flow
  - target: context/stack.md
    condition: when a choice affects libraries or runtime
  - target: context/conventions.md
    condition: when a choice affects implementation style
grounds_to: []
last_updated: 2026-09-28
---

# Decisions

## Decision Log

### Load local environment configuration before model initialization
**Date:** 2026-09-28
**Status:** Active
**Decision:** Call `load_dotenv()` before constructing the Gemini client.
**Reasoning:** The client reads `GOOGLE_API_KEY` from the process during module initialization; the original rationale is `[TO DETERMINE]`.
**Alternatives considered:** Reading the key inside `chat()` is not used by the current implementation.
**Consequences:** Configuration must be available before `app.py` finishes importing.

### Use LangChain messages for conversation history
**Date:** 2026-09-28
**Status:** Active
**Decision:** Represent prior turns and the current input as `HumanMessage` instances before invocation.
**Reasoning:** This is the current model boundary; the rationale for choosing LangChain over direct provider messages is `[TO DETERMINE]`.
**Alternatives considered:** Direct provider SDK calls are not present.
**Consequences:** Changes to history handling must preserve message ordering and the callback contract.

### Use Gradio ChatInterface as the UI boundary
**Date:** 2026-09-28
**Status:** Active
**Decision:** Expose the chatbot through `gr.ChatInterface(fn=chat, ...)` and launch it from the module entry point.
**Reasoning:** This is the current user-facing integration; the rationale for choosing Gradio is `[TO DETERMINE]`.
**Alternatives considered:** No alternate UI framework is present.
**Consequences:** UI behavior is coupled to the `chat(message, history)` callback signature.
