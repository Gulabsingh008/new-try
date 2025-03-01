from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

if __name__ == "__main__":
    app.start()
    print("✅ Bot Started Successfully!")
    idle()  # बॉट को रनिंग रखने के लिए
    app.stop()
