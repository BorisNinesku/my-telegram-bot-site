from telegram.ext import Application, CommandHandler
import os

async def start(update, context):
    await update.message.reply_text("Привет! Это мой бот.")

def main():
    app = Application.builder().token(os.getenv("BOT_TOKEN")).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == '__main__':
    main()