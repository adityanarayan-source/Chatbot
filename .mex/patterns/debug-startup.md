---
name: debug-startup
description: Diagnose startup, dependency, credential, and first-request failures.
triggers:
  - "debug startup"
  - "app will not launch"
  - "API key error"
edges:
  - target: context/setup.md
    condition: when checking prerequisites and environment configuration
  - target: context/architecture.md
    condition: when tracing the model and UI startup boundary
  - target: patterns/configure-gemini.md
    condition: when the failure is in model integration
grounds_to:
  - node: "function:1a1a0b31a2e453a40b034788c9d09f84"
    fingerprint: "mh:64:7b226d696e68617368223a5b31383134343139392c3130373232303930392c3232333231373531332c35313335313737382c3132313330333834372c3137313038313031312c3131303031383138372c38373735373730362c3131323435393630332c3230383839383938342c31373931303839362c34343432303330362c3330303532363131302c33393836313839382c3332323931353234352c32373732313037342c37313636333337362c373535353739342c3130363832303631332c3131353137353135382c3132353432313235382c3137313930383334352c313830393030342c393832393038372c39373435303534342c3134353337373332302c3334383434343538322c35313532323032362c3138373233373630332c313634363838322c3237313535343735322c3134363731353938312c343431393134332c35363434373436342c35383432383038362c3433343230343936342c3131303731353836362c31303836393338392c35363936323936392c3232323637313730362c36353530383733302c3132363231303135342c34303530343638372c3330393034333236312c353630353534392c3132393138363339382c3339383634353135382c34363739363633322c3135303730303839302c3130313333343538382c3435373231363931312c3132343839393236302c34313638303530332c3133393832373932312c3138343033393938312c37383932363934362c3131373238333032392c33343130313934382c3232333035303135312c35303733303035362c34333834393337302c37373637393735362c323935333732322c31313732363932355d2c226e65696768626f7273223a5b5d2c22746f6b656e436f756e74223a36397d"
last_updated: 2026-09-28
---

# Debug Startup

## Context
Startup performs dotenv loading, model construction, Gradio interface construction, and launch. The first request enters [`chat()`](mex://function:1a1a0b31a2e453a40b034788c9d09f84).

## Steps
1. Run `python -m py_compile app.py`.
2. Confirm all imported packages are installed in the active Python environment.
3. Confirm `GOOGLE_API_KEY` is present before running `python app.py`.
4. Separate import/model errors from Gradio launch errors.
5. For a first-request failure, inspect message assembly and model invocation.

## Gotchas
- There is no explicit API-key validation or error wrapper in the indexed implementation.
- No project test runner or linter is declared, so syntax compilation is the available local check.

## Verify
- [ ] The failure boundary is identified as import, model construction, launch, or request handling.
- [ ] Configuration values are not printed or committed.
- [ ] `python -m py_compile app.py` passes after a fix.

## Debug
Use the earliest failing boundary: imports, dotenv/model construction, Gradio creation, launch, then callback invocation.
