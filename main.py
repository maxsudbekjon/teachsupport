from fastapi import FastAPI, Form
import requests

app = FastAPI()

BOT_TOKEN = "8282184612:AAGc0QCUpyD21zGRM9QPmo9F6juzCaSrxi8"
CHAT_ID = "6779002546"

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
