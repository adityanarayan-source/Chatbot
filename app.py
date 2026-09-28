import os
import gradio as gr
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# Load environment variables
load_dotenv()

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7,
)


def chat(message, history):
    """Generate a response using Gemini."""
    messages = []

    # Add previous conversation
    for user_msg, assistant_msg in history:
        messages.append(HumanMessage(content=user_msg))
        messages.append(HumanMessage(content=assistant_msg))

    # Add current user message
    messages.append(HumanMessage(content=message))

    response = llm.invoke(messages)

    return response.content


# Gradio UI
demo = gr.ChatInterface(
    fn=chat,
    title="Gemini Chatbot",
    description="Simple chatbot using Python, LangChain and Gemini.",
    textbox=gr.Textbox(
        placeholder="Ask something...",
        container=True
    ),
)

# Start application
if __name__ == "__main__":
    demo.launch()