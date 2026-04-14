from flask import Flask, request

app = Flask(__name__)

@app.route("/") # http://127.0.0.1:8000/ або localhost:8000/
def hello_world(): # Перевірка обробки запитів сервером
    return "Hello World!"

@app.route("/currency") # http://127.0.0.1:8000/currency або localhost:8000/currency
def currency_static(): # Видає курс долара при запиті /currency?today&key=value
    key = request.args.get('key')  # Обробляє запит key=value
    date = 'today' in request.args  # Перевіряє чи є запит today в URL
    if not key or not date:
        return "Помилка! Параметри не були задані", 400

    return "USD = 41,5"


if __name__ == '__main__': # Запуск сервера на порті 8000
    app.run(port=8000)

