import json
import requests

TOKEN = "YOUR_BOT_TOKEN"

def handler(request):
    try:
        update = request.json()

        if "message" in update:
            chat_id = update["message"]["chat"]["id"]
            text = update["message"].get("text", "")

            requests.post(
                f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                data={
                    "chat_id": chat_id,
                    "text": f"شما گفتید:\n{text}"
                }
            )

        return {
            "statusCode": 200,
            "body": json.dumps({"ok": True})
        }

    except Exception as e:
        return {
            "statusCode": 200,
            "body": json.dumps({"error": str(e)})
        }