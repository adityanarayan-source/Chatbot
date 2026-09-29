# MEX Chatbot Demo

Simple chatbot POC using **Python, Gradio, LangChain, and Google Gemini**, with **MEX** used for persistent project memory for AI coding agents.

## Stack

- Python
- Gradio
- LangChain
- Google Gemini
- MEX `0.8.2`
- Git / GitHub

## 1. Run the Chatbot

```bash
git clone https://github.com/adityanarayan-source/Chatbot.git
cd Chatbot
python -m venv .venv
```

### Windows

```powershell
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

Create `.env` in the project root:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

Run:

```bash
python app.py
```

## 2. Setup MEX

Install MEX:

```bash
npm install -g mex-agent@0.8.2
```

Initialize from the project root:

```bash
npx mex-agent@0.8.2 setup
```

Check the setup:

```bash
mex check
```

Test the code graph:

```bash
mex graph scope "chatbot application" --fingerprint
```

## 3. Verify MEX Memory

1. Commit and push the MEX project-memory files to Git.
2. Clone the repository into a fresh folder.
3. Open the project in a fresh AI coding session.
4. Verify that the project purpose, structure, decisions, and conventions can be recovered without the previous chat history.

The POC was validated with **100/100, 0 errors, 0 warnings**.

## Notes

- Do **not** commit `.env` or API keys.
- Keep the local `.mex/graph.db` out of Git.
- MEX is the project's persistent engineering/project-memory layer; it is not the complete self-learning engine.

## Repository

https://github.com/adityanarayan-source/Chatbot
