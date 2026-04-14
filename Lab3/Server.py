from flask import Flask, request, jsonify, make_response
from functools import wraps
import json
import os

USERS_FILE = 'users.json'
SHOP_FILE = 'items.json'

app = Flask(__name__)

# Блок роботи з файлами
def load_users(): # Зчитання даних з файлу
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_users(users): # Збереження даних в файл
    with open(USERS_FILE, 'w', encoding='utf-8') as f:
        json.dump(users, f, indent=2, ensure_ascii=False)

def load_items():
    if not os.path.exists(SHOP_FILE):
        return []
    with open(SHOP_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_items(items):
    with open(SHOP_FILE, 'w', encoding='utf-8') as f:
        json.dump(items, f, indent=2, ensure_ascii=False)

# Блок авторизації
def check_auth(username, password): # Перевірка наявності користувача
    users = load_users()
    for u in users:
        if u.get('username') == username and u.get('password') == password:
            return True
    return False

def authenticate(): # Надсилає повідомлення та формує відповідь 401
    resp = make_response(jsonify({'message': 'Authentication required'}), 401)
    resp.headers['WWW-Authenticate'] = 'Basic realm="Login Required"'
    return resp

def requires_auth(f): # Вимогає авторизації для подальших дій
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

# Блок API
@app.route('/items', methods=['GET', 'POST'])
@requires_auth
def items():
    items = load_items()
    if request.method == 'GET': # Виводить каталог
        return jsonify(items)

    data = request.get_json(force=True) # Отримання файла з POST запиту
    if not data or 'id' not in data: # Перевірка файла на наявність ID
        return jsonify({'message': 'Item must contain an `id` field'}), 400
    if any(str(it.get('id')) == str(data['id']) for it in items): # Перевірка дублікатів ID
        return jsonify({'message': 'Item with this id already exists'}), 400
    items.append(data)
    save_items(items)
    return jsonify(data), 201

@app.route('/items/<item_id>', methods=['GET', 'PUT', 'DELETE'])
@requires_auth
def item_by_id(item_id):
    items = load_items()
    found = next((it for it in items if str(it.get('id')) == str(item_id)), None) # Знаходження блоку по ID

    if request.method == 'GET':
        if not found:
            return jsonify({'message': 'Not found'}), 404
        return jsonify(found)

    if request.method == 'PUT':
        if not found:
            return jsonify({'message': 'Not found'}), 404
        data = request.get_json(force=True)
        for k, v in data.items(): # Оновлення каталогу
            found[k] = v
        save_items(items)
        return jsonify(found)

    if request.method == 'DELETE':
        if not found:
            return jsonify({'message': 'Not found'}), 404
        items = [it for it in items if str(it.get('id')) != str(item_id)]
        save_items(items)
        return jsonify({'message': 'Deleted'})

    return jsonify({'message': 'Method not allowed'}), 405 #

# Блок ініціалізації сервера
if __name__ == '__main__':
    # create default users/items if missing (for convenience)
    if not os.path.exists(USERS_FILE):
        default_users = [{"username": "admin", "password": "password123"}]
        save_users(default_users)
        print('Created example users.json with username "admin" and password "password123"')

    if not os.path.exists(SHOP_FILE):
        default_items = [
            {"id": "1", "name": "T-shirt", "price": 4.99, "color": "blue"},
            {"id": "2", "name": "Jeans", "price": 14.99, "size": "M"}
        ]
        save_items(default_items)
        print('Created example items.json')

    app.run(host='0.0.0.0', port=8000, debug=True)