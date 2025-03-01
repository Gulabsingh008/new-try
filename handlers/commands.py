# handlers/commands.py - Handle All Commands
from pyrogram import Client, filters
from database import get_random_file
from config import LOG_CHANNEL_ID, OWNER_ID

@Client.on_message(filters.command("start") & filters.incoming)
async def start(client, message):
    await message.reply_text("Hello! Welcome to the bot. Use /today to get a random file.")

@Client.on_message(filters.command("today") & filters.incoming)
async def today(client, message):
    file = get_random_file()
    if file:
        await message.reply_document(file["file_id"], caption=file["file_name"])
    else:
        await message.reply_text("No files available.")

async def send_startup_notifications(client):
    startup_message = "✅ Bot Started Successfully!"
    try:
        # Notify Log Channel
        if LOG_CHANNEL_ID:
            await client.send_message(LOG_CHANNEL_ID, startup_message)
        # Notify Owner
        if OWNER_ID:
            await client.send_message(OWNER_ID, startup_message)
    except Exception as e:
        print(f"Error sending startup notification: {e}")
