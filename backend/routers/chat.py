from fastapi import APIRouter
from models.schemas import ChatMessage
from utils.groq_client import client, MODEL_CONFIG

router = APIRouter()


@router.post("/chat")
async def chat_with_papers(message: ChatMessage):

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a research assistant."
            },
            {
                "role": "user",
                "content": message.content
            }
        ],
        **MODEL_CONFIG
    )

    return {
        "response": response.choices[0].message.content
    }