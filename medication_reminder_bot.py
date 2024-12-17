import os
import asyncio
from telegram import Bot
from telegram.error import TelegramError
from datetime import datetime

# Retrieve bot token, group chat ID, and message index from environment variables
BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')
MESSAGE_INDEX = os.environ.get('MESSAGE_INDEX', "0")  # Default to 0 if not set

# Medication reminder messages
REMINDER_MESSAGES = [
    "Subah ki Dwaai khaa li kya!",
    "Dupehar ki dwaai khaa li kya ",
    "Khana & Raat ki dwaai kha li kya 💊"
]

async def send_medication_reminder():
    """Send a medication reminder to the specified group chat."""
    # Validate bot token and chat ID
    if not BOT_TOKEN or not CHAT_ID:
        print("Error: Missing TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID.")
        return
    
    # Validate message index
    if MESSAGE_INDEX is None or MESSAGE_INDEX.strip() == "" or not MESSAGE_INDEX.isdigit():
        print("Error: Missing or invalid MESSAGE_INDEX.")
        return
    
    message_index = int(MESSAGE_INDEX)
    if message_index < 0 or message_index >= len(REMINDER_MESSAGES):
        print("Error: MESSAGE_INDEX is out of range.")
        return

    # Initialize the bot and send the message
    bot = Bot(token=BOT_TOKEN)
    now = datetime.now().strftime("%H:%M %p")  # Current time
    message = f"{REMINDER_MESSAGES[message_index]} (Sent at {now})"

    try:
        await bot.send_message(chat_id=CHAT_ID, text=message)
        print(f"Sent reminder: {message}")
    except TelegramError as e:
        print(f"Telegram Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == '__main__':
    asyncio.run(send_medication_reminder())
