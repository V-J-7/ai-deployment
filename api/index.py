import os
from dotenv import load_dotenv
from fastapi import FastAPI  # type: ignore
from fastapi.responses import PlainTextResponse  # type: ignore
from openai import OpenAI  # type: ignore

load_dotenv()
app = FastAPI()
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

@app.get("/api", response_class=PlainTextResponse)
def idea():
    prompt = [{"role": "user", "content": "Come up with a new business idea for AI Agents"}]
    response = client.chat.completions.create(model="gemini-3.5-flash-lite", messages=prompt)
    return response.choices[0].message.content
