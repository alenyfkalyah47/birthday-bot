import os
from flask import Flask, request, jsonify
from telegram import Bot
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

bot = Bot(token=BOT_TOKEN)

app = Flask(__name__)

@app.route("/")
def home():
    return "Birthday Bot is running ❤️"

@app.route("/submit", methods=["POST"])
async def submit():

    data = request.get_json()

    name = data.get("name", "")
    attend = data.get("attend", "")
    count = data.get("count", "")
    drinks = ", ".join(data.get("drinks", []))
    comment = data.get("comment", "")

    text = f"""
🎉 Новое подтверждение присутствия

👤 Имя:
{name}

✅ Придет:
{attend}

👥 Количество гостей:
{count}

🍾 Напитки:
{drinks}

💬 Комментарий:
{comment}
"""

   import asyncio

asyncio.run(bot.send_message(
        chat_id=ADMIN_ID,
        text=text
    ))

    return jsonify({
        "success": True
    })
