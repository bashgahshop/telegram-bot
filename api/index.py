from fastapi import FastAPI, Request
import requests

app = FastAPI()

TOKEN = "1908448673:AAFi1_5jK54SbxstTZu_vtZ7mPLCxehSj18"

@app.get("/")
def home():
    return {"status": "OK"}

@app.post("/")
async def telegram(request: Request):
    update = await request.json()

    if "message" in update:
        chat_id = update["message"]["chat"]["id"]
        text = update["message"].get("text", "")

        requests.post(
            f"https://api.telegram.org/bot{TOKEN}/sendMessage",
            data={
                "chat_id": chat_id,
                "text": "شما گفتید:\n" + text
            }
        )

    return {"ok": True}