import os

from heroku3 import from_key
from pyrogram import Client

API_ID = int(os.environ.get("API_ID", "18891187"))
API_HASH = os.environ.get("API_HASH", "7d120384f48b2a86fa2b9e9772a28af6")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5179683696:AAFMoqtYwDWH2rhjELNLvuITskDX5gk4InY")
ARQ_API_KEY = "AQNBOO-IUZKEA-XNSPAM-DWFVBF-ARQ" 
LANGUAGE = "en"
ARQ_API_BASE_URL = "https://thearq.tech"

bot = Client(":memory:",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN)
