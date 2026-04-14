from telethon import TelegramClient
import asyncio

api_id = 1234567 # Ввести свій ID облікового запису
api_hash = "your_api_hash" # Ввести свій Hash
chat_username = "username or id" # Ввести потрібний телеграм чат (назва або id)

# Параметри відправки повідомлень
recipient = "username or id" # Ввести назву чату або id
message = "wanted message" # Ввести бажане повідомлення

async def main():
    # Отримання переліку користувачів в чаті
    client = TelegramClient("session 1", api_id, api_hash)
    await client.start()

    participants = await client.get_participants(chat_username)
    print(f"Учасників у чаті: {len(participants)}")

    for user in participants:
        print(user.id, user.username)

    input("Press Enter to continue...") # Перехід на наступну частину

    # Відправка повідомлення чату
    await client.send_message(recipient, message)
    print("Повідомлення відправлено!")

    await client.disconnect()

asyncio.run(main())
