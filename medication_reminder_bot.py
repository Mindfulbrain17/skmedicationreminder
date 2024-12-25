import os
import asyncio
from telegram import Bot

# Retrieve bot token and group chat ID from environment variables
BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

# Medication reminder messages
REMINDER_MESSAGES = [
    "Subah ki Dwaai khaa li kya!",
    "Dupehar ki dwaai khaa li kya",
    "Khana khaa liya kya"
]

async def send_evening_reminder():
    """Send the evening medication reminder."""
    # Validate bot token and chat ID
    if not BOT_TOKEN or not CHAT_ID:
        print("Error: Missing TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID.")
        return

    # Hardcode the message index to 2 for evening reminder
    message_index = 2

    # Initialize the bot and send the message
    bot = Bot(token=BOT_TOKEN)
    message = REMINDER_MESSAGES[message_index]
    try:
        await bot.send_message(chat_id=CHAT_ID, text=message)
        print(f"Sent reminder: {message}")
    except Exception as e:
        print(f"Error sending reminder: {e}")

if __name__ == '__main__':
    asyncio.run(send_evening_reminder())
