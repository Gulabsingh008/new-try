from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from pyrogram.errors import RPCError
from pyrogram import idle


app = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

import handlers.commands  # All commands in one file

if __name__ == "__main__":
    try:
        app.start()
        print("Bot is running...")
        idle()  # Keeps the bot running
    except RPCError as e:
        print(f"Error: {e}")
    finally:
        app.stop()
        print("Bot stopped.")
