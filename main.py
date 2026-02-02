from fastapi import FastAPI
from pydantic import BaseModel
import os
from groq import Groq
from fastapi.middleware.cors import CORSMiddleware

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://chatbot369.netlify.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Mess(BaseModel):
    message: str

def verify(mess: str):
    chat_completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": mess}],
    )
    return chat_completion.choices[0].message.content

@app.post("/chat")
async def chat(res: Mess):
    return {"Message": verify(res.message.lower())}