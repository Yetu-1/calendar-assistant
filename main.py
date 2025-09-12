import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from openai import AsyncOpenAI
from agents import Runner
from calendar_agent import calendar_agent

load_dotenv()
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

class Chat(BaseModel):
    query: str | None = None


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/assistant")
async def root(message: Chat):
    response = await Runner.run(calendar_agent, message.query)
    return {"response": response.final_output}