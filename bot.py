import os
import requests

from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Birthday Bot is running ❤️"


@app.route("/submit", methods=["POST"])
def submit():

    data = request.get_json()

    name = data.get("name", "")
    attend = data.get("attend", "")
    count = data.get("count", "")
    drinks = ", ".join(data.get("drinks", []))
    comment = data.get("comment", "")
    other_drink = data.get("otherDrink", "")

    text = f"""🎉 Новое подтверждение

👤 Имя: {name}

✅ Присутствие: {attend}

👥 Количество гостей: {count}

🍾 Напитки: {drinks}

🍹 Другой напиток:
{other_drink if other_drink else "—"}

💬 Комментарий:
{comment}
"""

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={
            "chat_id": ADMIN_ID,
            "text": text,
        },
        timeout=15,
    )

    return jsonify({"success": True})
