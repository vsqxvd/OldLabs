import requests
from requests.auth import HTTPBasicAuth

BASE = 'http://127.0.0.1:8000'
USERNAME = 'admin'
PASSWORD = 'password123'

def list_items():
    r = requests.get(f'{BASE}/items', auth=HTTPBasicAuth(USERNAME, PASSWORD))
    return r.status_code, r.json()

def get_item(item_id):
    r = requests.get(f'{BASE}/items/{item_id}', auth=HTTPBasicAuth(USERNAME, PASSWORD))
    return r.status_code, r.json()

def create_item(item):
    r = requests.post(f'{BASE}/items', json=item, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    return r.status_code, r.json()

def update_item(item_id, data):
    r = requests.put(f'{BASE}/items/{item_id}', json=data, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    return r.status_code, r.json()

def delete_item(item_id):
    r = requests.delete(f'{BASE}/items/{item_id}', auth=HTTPBasicAuth(USERNAME, PASSWORD))
    return r.status_code, r.json()

if __name__ == '__main__': # Перевірка роботи серверу з клієнтом
    print('Listing items:')
    print(list_items())

    print('\nCreating item id=3:')
    print(create_item({"id": "3", "name": "Coat", "price": 1.5}))

    print('\nGetting item id=3:')
    print(get_item('3'))

    print('\nUpdating item id=3:')
    print(update_item('3', {"price": 44.99, "color": "Black"}))

    print('\nDeleting item id=3:')
    print(delete_item('3'))