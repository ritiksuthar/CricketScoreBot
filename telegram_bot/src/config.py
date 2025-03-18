import os
from dotenv import load_dotenv

load_dotenv()  # .env file load karega

BOT_API_TOKEN = os.getenv("BOT_API_TOKEN")
CRICKET_API_URL = "https://api.cricapi.com/v1/currentMatches"
CRICKET_API_KEY = os.getenv("CRICKET_API_KEY")
