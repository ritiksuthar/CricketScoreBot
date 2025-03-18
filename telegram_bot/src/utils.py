from apscheduler.schedulers.background import BackgroundScheduler
from cricket_api import get_live_scores
from telegram import Bot
from config import BOT_API_TOKEN
import asyncio

bot = Bot(token=BOT_API_TOKEN)
scheduler = BackgroundScheduler()

# Auto-update function
async def send_score_updates(chat_id):
    scores = get_live_scores()
    await bot.send_message(chat_id=chat_id, text=f"📢 Live Cricket Update:\n{scores}")

# Scheduler ko shuru karne ka function
def start_scheduler(chat_id):
    loop = asyncio.get_event_loop()
    scheduler.add_job(lambda: asyncio.run_coroutine_threadsafe(send_score_updates(chat_id), loop), 'interval', minutes=5)
    scheduler.start()
