import os
import logging
import sqlite3

import gradio as gr
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage

# Load environment variables
load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATABASE_PATH = os.getenv("CHAT_DATABASE", "chat_history.db")


def initialize_database():
    """Create the SQLite table used to persist messages for each Gradio session."""
    with sqlite3.connect(DATABASE_PATH) as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT NOT NULL,
                role TEXT NOT NULL CHECK(role IN ('user', 'assistant')),
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        connection.commit()


def load_session_messages(session_id):
    """Read the ordered conversation for one browser session."""
    with sqlite3.connect(DATABASE_PATH) as connection:
        rows = connection.execute(
            "SELECT role, content FROM messages WHERE session_id = ? ORDER BY id",
            (session_id,),
        ).fetchall()
    return rows


def save_session_messages(session_id, messages):
    """Append messages to a browser session's SQLite history."""
    if not messages:
        return

    with sqlite3.connect(DATABASE_PATH) as connection:
        connection.executemany(
            "INSERT INTO messages (session_id, role, content) VALUES (?, ?, ?)",
            [(session_id, role, content) for role, content in messages],
        )
        connection.commit()


def normalize_history(history):
    """Support Gradio's OpenAI-style history and older tuple-based history."""
    normalized = []
    for item in history or []:
        if isinstance(item, dict):
            role = item.get("role")
            content = item.get("content")
            if role in ("user", "assistant") and isinstance(content, str):
                normalized.append((role, content))
        elif isinstance(item, (list, tuple)) and len(item) == 2:
            user_message, assistant_message = item
            if isinstance(user_message, str):
                normalized.append(("user", user_message))
            if isinstance(assistant_message, str):
                normalized.append(("assistant", assistant_message))
    return normalized


initialize_database()

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(
    model=os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite"),
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7,
)


def chat(message, history, request: gr.Request | None = None):
    """Generate a response using Gemini."""
    session_id = getattr(request, "session_hash", None) or "local-session"
    stored_history = load_session_messages(session_id)
    received_history = normalize_history(history)

    # Seed the database if Gradio already has history from before this process
    # started, then use SQLite as the source of truth for this session.
    if not stored_history and received_history:
        save_session_messages(session_id, received_history)
        stored_history = received_history

    messages = [
        AIMessage(content=content) if role == "assistant"
        else HumanMessage(content=content)
        for role, content in stored_history
    ]

    # Add current user message
    messages.append(HumanMessage(content=message))

    try:
        response = llm.invoke(messages)
    except Exception:
        logger.exception("Gemini request failed for session %s", session_id)
        return "I couldn't reach Gemini right now. Please check the API key and network connection, then try again."

    content = response.content
    if isinstance(content, list):
        content = "".join(
            item.get("text", "") if isinstance(item, dict) else str(item)
            for item in content
        )
    content = str(content)

    save_session_messages(
        session_id,
        [("user", message), ("assistant", content)],
    )

    return content


# Gradio UI
demo = gr.ChatInterface(
    fn=chat,
    title="Gemini Chatbot",
    description="Simple chatbot using Python, LangChain and Gemini.",
    textbox=gr.Textbox(
        placeholder="Ask something...",
        container=True
    ),
    save_history=True,
)

# Start application
if __name__ == "__main__":
    demo.launch()
