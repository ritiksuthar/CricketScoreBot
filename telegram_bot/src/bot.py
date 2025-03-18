from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler
from config import BOT_API_TOKEN
from handlers import start, help_command, score, subscribe, unsubscribe
import os

def main():
    app = ApplicationBuilder().token(BOT_API_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("score", score))
    app.add_handler(CommandHandler("subscribe", subscribe))
    app.add_handler(CommandHandler("unsubscribe", unsubscribe))



    print("Bot is running...")
    # Port Configuration for Render Deployment
    port = int(os.environ.get("PORT", 8443))  # Default HTTPS port
    webhook_url = f"https://{os.environ.get('RENDER_EXTERNAL_HOSTNAME')}/"  # Render-specific domain

    app.run_webhook(
        listen="0.0.0.0",
        port=port,
        url_path=BOT_API_TOKEN,
        webhook_url=webhook_url + BOT_API_TOKEN
    )
if __name__ == "__main__":
    main()
