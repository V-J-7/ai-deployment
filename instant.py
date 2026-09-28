from fastapi import FastAPI
from openai import OpenAI
from starlette.responses import HTMLResponse

app = FastAPI()
client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
@app.get("/", response_class = HTMLResponse)
def instant():
    message = """
    You are on a website that has just been deployed to production for the first time
    Reply with an enthusiastic announcement to welcome visitors to the site, explaining that it is live on production for the first time
    """
    messages = [{"role": "user", "content": message}]
    response = client.chat.completions.create(model="gemini-3.5-flash", messages=messages)
    reply = response.choices[0].message.content.replace("\n", "<br/>")
    html = f"<html><head><title>Live in an Instant!</title></head><body><p>{reply}</p></body></html>"
    return html