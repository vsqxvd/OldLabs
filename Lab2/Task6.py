from flask import Flask, request, jsonify, Response
import requests
from datetime import datetime, timedelta
import sqlite3

app = Flask(__name__)

def init_db(): # Ініціалізація бази даних sqlite3
    conn = sqlite3.connect("my_data.db")
    c = conn.cursor()
    c.execute('''
              CREATE TABLE IF NOT EXISTS messages
              (
                  id
                  INTEGER
                  PRIMARY
                  KEY
                  AUTOINCREMENT,
                  text
                  TEXT,
                  date
                  TEXT
              )
              ''')
    conn.commit()
    conn.close()

init_db()

@app.route("/", methods=["GET"])
def index(): # Створення сторінки, де можна вписати дані
    return """
    <!doctype html>
    <html>
        <head>
            <title>Збереження тексту</title>
        </head>
        <body>
            <h1>Введіть текст для збереження у файл</h1>
            <form method="post" action="/save_file">
                <textarea name="text" rows="5" cols="50"></textarea><br><br>
                <input type="submit" value="Відправити">
            </form>
        </body>
    </html>
    """

@app.route("/save_file", methods=["GET", "POST"])
def save_file():
    message = ""

    # Збереження у файл
    if request.method == "POST":
        text = request.form.get("text")
        if not text:
            message = "Помилка! Текст не введено"
        else:
            with open("my_data.txt", "a", encoding="utf-8") as f:
                f.write(f"{datetime.now()}: {text}\n")

    # Збереження у базу даних
    conn = sqlite3.connect("my_data.db")
    c = conn.cursor()
    c.execute("INSERT INTO messages (text, date) VALUES (?, ?)", (text, datetime.now()))
    conn.commit()
    conn.close()

    return f'''
            <h3>Дані успішно збережено!</h3>
            <p>Дані, що були надані: <b>{text}</b></p>
            <ul>
                <li>Записано у файл: "my_data.txt"</li>
                <li>Записано у базу даних: "my_data.db"</li>
            </ul>
            <br>
            <a href="/">Повернутися назад</a>
        '''


if __name__ == '__main__': # Запуск сервера на порті 8000
    app.run(port=8000)
