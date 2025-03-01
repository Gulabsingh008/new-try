# handlers/commands.py - Handle All Commands
from pyrogram import Client, filters
from database import get_random_file

def start_command(client, message):
    message.reply_text("Hello! Welcome to the bot. Use /today to get a random file.")

def today_command(client, message):
    file = get_random_file()
    if file:
        message.reply_document(file["file_id"], caption=file["file_name"])
    else:
        message.reply_text("No files available.")

app.add_handler(filters.command("start")(start_command))
app.add_handler(filters.command("today")(today_command))
