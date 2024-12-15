import os
import asyncio
from telegram import Bot

# Retrieve bot token, group chat ID, and message index from environment variables
BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')
MESSAGE_INDEX = os.environ.get('MESSAGE_INDEX')  # Determines which message to send

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
    if MESSAGE_INDEX is None or not MESSAGE_INDEX.isdigit():
        print("Error: Missing or invalid MESSAGE_INDEX.")
        return
    
    message_index = int(MESSAGE_INDEX)
    if message_index < 0 or message_index >= len(REMINDER_MESSAGES):
        print("Error: MESSAGE_INDEX is out of range.")
        return

    # Initialize the bot and send the message
    bot = Bot(token=BOT_TOKEN)
    message = REMINDER_MESSAGES[message_index]
    try:
        await bot.send_message(chat_id=CHAT_ID, text=message)
        print(f"Sent reminder: {message}")
    except Exception as e:
        print(f"Error sending reminder: {e}")

if __name__ == '__main__':
    asyncio.run(send_medication_reminder())
