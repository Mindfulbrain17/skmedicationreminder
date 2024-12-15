import os
import asyncio
from telegram import Bot
from telegram.ext import Application

# Retrieve bot token and group chat ID from environment variables
BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

# Medication reminder messages
REMINDER_MESSAGES = [
    "Hey, it's time to take your morning medication! 💊",
    "Time for your afternoon medication! 💊",
    "Don't forget your evening medication before bed! 💊"
]

async def send_medication_reminder(bot, message):
    """Send a medication reminder to the specified group chat."""
    try:
        await bot.send_message(chat_id=CHAT_ID, text=message)
        print(f"Sent reminder: {message}")
    except Exception as e:
        print(f"Error sending reminder: {e}")

async def main():
    """Main function to set up and send medication reminders."""
    # Validate environment variables
    if not BOT_TOKEN or not CHAT_ID:
        print("Error: Missing Telegram Bot Token or Chat ID")
        return

    # Initialize the Telegram bot
    bot = Bot(token=BOT_TOKEN)

    # Send morning reminder
    await send_medication_reminder(bot, REMINDER_MESSAGES[0])

if __name__ == '__main__':
    asyncio.run(main())
