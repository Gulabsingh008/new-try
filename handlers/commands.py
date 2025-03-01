# handlers/commands.py - Handle All Commands
from pyrogram import Client, filters
from database import get_random_file

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
