from flask import Flask
from dotenv import load_dotenv
import os
from os.path import join, dirname

app = Flask(__name__)


def get_secret(key):
    # возвращает секретный токен
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    return os.environ.get(key)


@app.route('/')
def hello_world():
    # основная функция
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()
