import os

from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()


def create_chatbot():
    token = os.getenv("HF_TOKEN")

    if not token:
        raise ValueError("HF_TOKEN is not set")

    llm = HuggingFaceEndpoint(
        repo_id="deepseek-ai/DeepSeek-V4-Flash-0731",
        huggingfacehub_api_token=token,
        task="text-generation",
    )

    return ChatHuggingFace(llm=llm)


def get_response(message: str) -> str:
    chatbot = create_chatbot()

    response = chatbot.invoke(message)

    return response.content