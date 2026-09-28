---
name: conventions
description: Coding and verification conventions observable in app.py.
triggers:
  - "convention"
  - "pattern"
  - "naming"
  - "style"
edges:
  - target: context/architecture.md
    condition: when a convention depends on the callback and UI flow
  - target: context/stack.md
    condition: when a convention concerns imported libraries
  - target: patterns/extend-chat.md
    condition: when modifying conversation behavior
grounds_to:
  - node: "function:1a1a0b31a2e453a40b034788c9d09f84"
    fingerprint: "mh:64:7b226d696e68617368223a5b31383134343139392c3130373232303930392c3232333231373531332c35313335313737382c3132313330333834372c3137313038313031312c3131303031383138372c38373735373730362c3131323435393630332c3230383839383938342c31373931303839362c34343432303330362c3330303532363131302c33393836313839382c3332323931353234352c32373732313037342c37313636333337362c373535353739342c3130363832303631332c3131353137353135382c3132353432313235382c3137313930383334352c313830393030342c393832393038372c39373435303534342c3134353337373332302c3334383434343538322c35313532323032362c3138373233373630332c313634363838322c3237313535343735322c3134363731353938312c343431393134332c35363434373436342c35383432383038362c3433343230343936342c3131303731353836362c31303836393338392c35363936323936392c3232323637313730362c36353530383733302c3132363231303135342c34303530343638372c3330393034333236312c353630353534392c3132393138363339382c3339383634353135382c34363739363633322c3135303730303839302c3130313333343538382c3435373231363931312c3132343839393236302c34313638303530332c3133393832373932312c3138343033393938312c37383932363934362c3131373238333032392c33343130313934382c3232333035303135312c35303733303035362c34333834393337302c37373637393735362c323935333732322c31313732363932355d2c226e65696768626f7273223a5b5d2c22746f6b656e436f756e74223a36397d"
last_updated: 2026-09-28
---

# Conventions

## Naming
- The application entry point is `app.py`.
- The callback is named `chat` and accepts `message, history`.
- The UI instance is named `demo`; the model client is named `llm`.

## Structure
- Configuration loading and model construction occur at module scope.
- Conversation assembly and model invocation stay inside `chat`.
- Gradio construction occurs after the callback and the launch guard is at the bottom of `app.py`.

## Patterns
- Preserve history order: append each user message followed by its assistant response, then append the current user message.
- Return model text through `response.content`, which is the callback's UI-facing result.

## Verify Checklist
- [ ] `app.py` still imports the four libraries used by the current implementation.
- [ ] `chat(message, history)` retains its two-argument callback shape.
- [ ] Prior history remains ordered before the current message.
- [ ] The model response is returned as text content.
- [ ] `gr.ChatInterface` still points to `chat`.
- [ ] `python -m py_compile app.py` passes.
