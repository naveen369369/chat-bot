from fastapi import FastAPI
from pydantic import BaseModel,Field
import os
from groq import Groq
from dotenv import load_dotenv   
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

load_dotenv()                   

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)


app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*", "http://localhost:5173"],  # temporarily "*" for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Mess(BaseModel):
    message:str

def verify(mess):
   chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": mess,
        }
    ],
    model="llama-3.3-70b-versatile",
   )

   return chat_completion.choices[0].message.content

@app.post("/chat")
async def chat(res:Mess):
     rest=verify(res.message.lower())
     return{
          "Message":rest
     }

app.mount(
    "/",
    StaticFiles(directory="Frontend/chatbot/dist", html=True),
    name="frontend"
)