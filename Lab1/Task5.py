from telegram.ext import Updater, CommandHandler

TOKEN = "Need bot token" # Введи свій токен телеграм боту

def start(update, context):
    update.message.reply_text("Введи /menu щоб дізнатись команди.")

def menu(update, context):
    commands = (
        "/menu — список команд\n"
        "/whisper текст — написати тихо\n"
        "/scream текст — прокричати"
    )
    update.message.reply_text(commands)

def whisper(update, context):
    if context.args:
        text = " ".join(context.args).lower()
        update.message.reply_text(text)
    else:
        update.message.reply_text("Введи будь-ласка текст після команди!")

def scream(update, context):
    if context.args:
        text = " ".join(context.args).upper()
        update.message.reply_text(text)
    else:
        update.message.reply_text("Введи будь-ласка текст після команди!")

def main():
    updater = Updater(TOKEN, use_context=True) # Підключення скрипту до бота
    dp = updater.dispatcher # Обробка запросів команд

    # Додавання команд боту
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("menu", menu))
    dp.add_handler(CommandHandler("whisper", whisper))
    dp.add_handler(CommandHandler("scream", scream))

    # Очікування ботом відправки запросів
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
