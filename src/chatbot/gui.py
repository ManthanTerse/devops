import gradio as gr

from chatbot.chatbot import get_response


def chat(message, history):
    return get_response(message)


demo = gr.ChatInterface(
    fn=chat,
    title="Simple LangChain Chatbot",
    description="Chatbot using LangChain and Hugging Face"
)


if __name__ == "__main__":
    demo.launch()