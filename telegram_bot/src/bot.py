from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler
from config import BOT_API_TOKEN
from handlers import start, help_command, score, subscribe, unsubscribe

def main():
    app = ApplicationBuilder().token(BOT_API_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("score", score))
    app.add_handler(CommandHandler("subscribe", subscribe))
    app.add_handler(CommandHandler("unsubscribe", unsubscribe))



    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
