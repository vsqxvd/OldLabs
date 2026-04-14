from flask import Flask, request, jsonify, Response

app = Flask(__name__)

@app.route("/") # http://127.0.0.1:8000/ або localhost:8000/
def hello_world(): # Перевірка обробки запитів сервером
    return "Hello World!"

@app.route("/currency") # http://127.0.0.1:8000/currency або localhost:8000/currency
def currency_static(): # Видає курс долара при запиті /currency?today&key=value
    value = {"USD" : 41.5}
    key = request.args.get('key')  # Обробляє запит key=value
    date = 'today' in request.args  # Перевіряє чи є запит today в URL
    content_type = request.headers.get("Content-Type")
    if not key or not date:
        return "Помилка! Параметри не були задані", 400

    form = request.args.get('format') # Створено для перевірки через браузер

    if form == "json":
        return jsonify(value)
    elif form == "xml":
        xml_data = f"<rates><USD>{value['USD']}</USD></rates>"
        return Response(xml_data, mimetype='application/xml')
    else:
        return "USD = 41,5"

    if content_type == "application/json": # Код для завдання
        return jsonify(value)
    elif content_type == "application/xml":
        xml_data = f"<rates><USD>{value['USD']}</USD></rates>"
        return Response(xml_data, mimetype='application/xml')
    else:
        return "USD = 41,5"



if __name__ == '__main__': # Запуск сервера на порті 8000
    app.run(port=8000)
