import requests
import matplotlib.pyplot as plt

url_API = f"https://bank.gov.ua/NBU_Exchange/exchange_site?json&valcode=usd&start=20251017&end=20251117"
response = requests.get(url_API) # Проводимо запит
date = []
val = []

if response.status_code == 200:
    currency = response.json() # Отримуємо дані в форматі JSON, якщо запит підтверджено
    for i in currency:
        date.append(i['exchangedate'])
        val.append(i['rate'])
else:
    print("Помилка запиту:", response.status_code) # Сповіщення помилки отримання запиту

plt.figure(figsize = (13.66,7.68))
plt.plot(date, val, marker='o')
plt.title("Курс USD")
plt.xlabel("Дата")
plt.ylabel("Курс, грн")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()