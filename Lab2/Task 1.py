from flask import Flask

app = Flask(__name__)

if __name__ == '__main__': # Запуск сервера на порті 8000
    app.run(port=8000)
