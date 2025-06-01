from fastapi import FastAPI, HTTPException
from schemas import Prompt
from ai_engine import OpenAIChatEngine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

chat_engine = OpenAIChatEngine()

@app.post("/chat")
async def chat_with_ai(prompt: Prompt):
    response = chat_engine.get_response(prompt.question)

    if "Invalid OpenAI API key" in response:
        raise HTTPException(status_code=400, detail="Invalid API key. Update your .env file.")

    elif "Unexpected Error" in response:
        raise HTTPException(status_code=500, detail=response)

    return {"answer": response}
