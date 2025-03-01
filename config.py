import os
from os import environ

API_ID = int(os.getenv("API_ID", 26494161))  # Replace with actual API_ID
API_HASH = os.getenv("API_HASH", "55da841f877d16a3a806169f3c5153d3")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7670198611:AAEUcnYA5ROmoor9TDB1NebOv8CQAO1Q7LM")

LOG_CHANNEL_ID = int(os.getenv("LOG_CHANNEL_ID", "-1002030723564"))  # लॉग चैनल ID
OWNER_ID = int(os.getenv("OWNER_ID", "7170452349"))  # ओनर का टेलीग्राम ID

DATABASE_URI = os.getenv("DATABASE_URI", "")
DATABASE_NAME = "af_data"
COLLECTION_NAME = "afcollection"
