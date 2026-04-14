from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world(): # Перевірка обробки запитів сервером 
    return "Hello World!"


if __name__ == '__main__': # Запуск сервера на порті 8000
    app.run(port=8000)

