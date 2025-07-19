from flask import Flask, request
import requests

# ✅ Set your bot token here directly
TOKEN = "7504653152:AAEtS7QPgdSe5VnUpiCU_GEJXq84i5qKJ4k"
URL = f"https://api.telegram.org/bot{TOKEN}/"

app = Flask(__name__)

def send_message(chat_id, text):
    requests.post(URL + "sendMessage", json={"chat_id": chat_id, "text": text})

@app.route("/", methods=["GET"])
def home():
    return "Bot is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        if text == "/start":
            send_message(chat_id, "👋 Hello! I'm alive on Railway!")
        else:
            send_message(chat_id, f"You said: {text}")
    return "OK", 200

if __name__ == "__main__":
    app.run(debug=True)
