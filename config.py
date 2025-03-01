# config.py - Store all bot configurations
import os

API_ID = int(os.getenv("API_ID", "26494161"))  # Replace with your API ID
API_HASH = os.getenv("API_HASH", "55da841f877d16a3a806169f3c5153d3")  # Replace with your API Hash
BOT_TOKEN = os.getenv("BOT_TOKEN", "7670198611:AAEUcnYA5ROmoor9TDB1NebOv8CQAO1Q7LM")  # Replace with your Bot Token

DATABASE_URI = os.getenv("DATABASE_URI", "")
DATABASE_NAME = "af_data"
COLLECTION_NAME = "afcollection"

LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1002030723564"))  # Channel where logs will be sent
