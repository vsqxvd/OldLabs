from flask import Flask, request, jsonify, Response
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route("/") # http://127.0.0.1:8000/ або localhost:8000/
def hello_world(): # Перевірка обробки запитів сервером
    return "Hello World!"

def get_usd_value(date): # Отримання курсу долару з сайту НБУ
    url = f"https://bank.gov.ua/NBU_Exchange/exchange_site?start={date}&end={date}&valcode=usd&json"

    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()
        if data:
            return data[0]['rate']
    return None

@app.route("/dynamic-currency")
def dynamic_currency(): # Встановлення даних параметром data
    date_check = request.args.get('data')
    if date_check == "today":
        date = datetime.now().strftime("%Y%m%d")
    elif date_check == "yesterday":
        date = (datetime.now()-timedelta(days=1)).strftime("%Y%m%d")
    else:
        return "Помилка! Невірний параметр data"

    rate = get_usd_value(date)
    if rate:
        return f"USD = {rate}"
    else:
        return "Помилка отримання курсу"


if __name__ == '__main__': # Запуск сервера на порті 8000
    app.run(port=8000)
