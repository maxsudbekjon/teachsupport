from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import requests
from dotenv import load_dotenv
import os

# .env faylni yuklaymiz
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

app = FastAPI()

def send_to_telegram(data):
    text = (
        f"🆕 Yangi so'rov:\n\n"
        f"👤 Ism: {data['name']}\n"
        f"🏢 Kompaniya: {data['company']}\n"
        f"📞 Kontakt: {data['contact']}\n"
        f"🧩 Stack: {data['stack']}\n"
        f"📝 Xabar: {data['message']}"
    )

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": text})


@app.post("/send-request")
def send_request(
    name: str = Form(...),
    company: str = Form(""),
    contact: str = Form(...),
    stack: str = Form(""),
    message: str = Form(...)
):
    data = {
        "name": name,
        "company": company,
        "contact": contact,
        "stack": stack,
        "message": message,
    }

    send_to_telegram(data)
    return {"status": "success"}


@app.get("/", response_class=HTMLResponse)
def serve_html():
    with open("sas.html", "r", encoding="utf-8") as f:
        return f.read()
