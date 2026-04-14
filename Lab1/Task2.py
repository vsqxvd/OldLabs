
# Запит курсу долару із сайту НБУ за попередній тиждень
url_API = f"https://bank.gov.ua/NBU_Exchange/exchange_site?json&valcode=usd&start=20251017&end=20251117"

import requests
response = requests.get(url_API) # Проводимо запит

if response.status_code == 200:
    currency = response.json() # Отримуємо дані в форматі JSON, якщо запит підтверджено
    print(f"Курс долара за попередній тиждень:")
    for i in currency:
        print(f"{i['exchangedate']} | {i['cc']} | {i['rate']}") # Виводимо фільтровані дані в термінал
else:
    print("Помилка запиту:", response.status_code) # Сповіщення помилки отримання запиту
