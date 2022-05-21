from flask import Flask, request
import requests
from dotenv import load_dotenv
import os
from os.path import join, dirname

app = Flask(__name__)


def get_secret(key):
    # возвращает секретный токен
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    return os.environ.get(key)


def send_message(chat_id, text):
    method = "sendMessage"
    token = get_secret("TELEGRAM_BOT_TOKEN")
    url = f'https://api.telegram.org/bot{token}/{method}'
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)


@app.route('/', methods=["GET", "POST"])
def main_app():
    # основная функция
    chat_id = request.json["message"]["chat"]["id"]
    if request.method == "POST":
        send_message(chat_id=chat_id, text="привет")
    return {"ok": True}


if __name__ == '__main__':
    app.run()
