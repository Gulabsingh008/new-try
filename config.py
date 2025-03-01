# config.py - Store all bot configurations
import os

API_ID = int(os.getenv("API_ID", "12345"))  # Replace with your API ID
API_HASH = os.getenv("API_HASH", "your_api_hash")  # Replace with your API Hash
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")  # Replace with your Bot Token

DATABASE_URI = os.getenv("DATABASE_URI", "mongodb+srv://your_mongo_uri")
DATABASE_NAME = "techvjclonefilterbot"
COLLECTION_NAME = "vjcollection"

LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1001234567890"))  # Channel where logs will be sent
