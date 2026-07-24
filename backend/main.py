import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

# Key loaded strictly from environment variable
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None

app = FastAPI(title="AIVOA Pharma QMS Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ComplaintRequest(BaseModel):
    description: str

@app.get("/")
def read_root():
    return {"status": "AIVOA Pharma QMS API is running"}

@app.post("/analyze-complaint")
def analyze_complaint(data: ComplaintRequest):
    if not client:
        raise HTTPException(status_code=500, detail="Groq API key not configured on server.")
    
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are an AI QMS Copilot for pharmaceutical complaint handling."
                },
                {
                    "role": "user",
                    "content": f"Analyze complaint:\n\n{data.description}"
                }
            ],
            temperature=0.3,
        )
        return {"analysis": completion.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))