from telegram import Update
from telegram.ext import ContextTypes
from cricket_api import get_live_scores
from utils import start_scheduler

subscribed_users = set()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏏 Welcome to Cricket Score Bot! Type /score to get live cricket updates.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Commands:\n/start - Start the bot\n/score - Get live cricket scores\n/help - For assistance")

async def score(update: Update, context: ContextTypes.DEFAULT_TYPE):
    scores = get_live_scores()
    await update.message.reply_text(scores)

async def subscribe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    if chat_id not in subscribed_users:
        subscribed_users.add(chat_id)
        start_scheduler(chat_id)
        await update.message.reply_text(" Subscribed for live score updates every 5 minutes!")
    else:
        await update.message.reply_text(" You're already subscribed!")

async def unsubscribe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    if chat_id in subscribed_users:
        subscribed_users.remove(chat_id)
        await update.message.reply_text(" Unsubscribed from live score updates.")
    else:
        await update.message.reply_text("You are not subscribed yet!")