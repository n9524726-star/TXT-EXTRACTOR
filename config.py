import os
from os import getenv

API_ID = int(os.environ.get("API_ID", "35524250"))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("API_HASH", "98de9f02ef055387a1cf3eda6220a18e")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

OWNER_ID = int(os.environ.get("OWNER_ID", "5200919974"))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "5200919974").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://sonickuwal_db_user:alfsMN6kIAt9qNQ1@cluster0.lqwg2ve.mongodb.net/?appName=Cluster0")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003086072844"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "-1003086072844")  # Optional here you'll get all logs
