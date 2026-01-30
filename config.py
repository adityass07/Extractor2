import os
from os import getenv

API_ID = int(os.environ.get("API_ID", "30929822"))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("API_HASH", "8586e9580c6480b65d23150cec959506")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

OWNER_ID = int(os.environ.get("OWNER_ID", "8342248523"))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "8365074618").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("MONGO_URL", "")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003654676671"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "-1003849481374")  # Optional here you'll get all logs
