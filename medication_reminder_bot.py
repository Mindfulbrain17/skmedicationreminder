import os
import asyncio
from telegram import Bot

# Retrieve bot token and chat ID from environment variables
BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

# Evening reminder messages (Random Generated Messages)
EVENING_MESSAGES = [
"Swati aur Anant, dinner ka scene set hai ya 'food Instagram influencers' ki research chal rahi hai?",
"AG, SK, khana plate mein hai ya 'online rating analysis paralysis' ho gaya?",
"SK aur AG, dinner khatam hua ya 'tiffin service detective work' mein lage hue ho?",
"Swati Kulshreshta and Anant Goyal, pet pooja ho gayi ya 'meal prep time travel' kar rahe ho?",
"AG aur SK, khaya ya abhi bhi 'cookbook consultation seminar' chal raha hai?",
"Swati aur Anant, dinner ho gaya ya 'kitchen gadget assembly challenge' complete nahi hua?",
"AG, SK, dinner complete hua ya 'food temperature perfection quest' mein ho?",
"SK aur AG, khana khaya ya 'mid-meal Netflix break' ne flow break kar diya?",
"Swati Kulshreshta and Anant Goyal, plates wash ho gaye ya 'dishwasher loading puzzle' solve kar rahe ho?",
"AG aur SK, dinner kha liya ya 'restaurant bill shock therapy' se bach rahe ho?",
"Swati aur Anant, pet bhar gaya ya abhi bhi 'virtual cooking class buffering' ho raha hai?"
"Swati Kulshreshta and Anant Goyal, aaj dinner mein khana hai ya abhi bhi 'food order pending' ka status hai?",
"AG aur SK, dinner pe khana aaya ya abhi bhi 'snack mode on' ka option hai?",
"Swati aur Anant, dinner complete hua ya abhi bhi 'kitchen ki kahaniyan' likh rahe ho?",
"AG, SK, khana kha liya ya abhi bhi 'cooking marathon' chal raha hai?",
"Swati Kulshreshta and Anant Goyal, dinner ka plan clear hai ya abhi bhi 'food delivery saga' chal raha hai?",
"AG aur SK, dinner table par khana hai ya abhi bhi 'order waiting game' chal raha hai?",
"Swati aur Anant, aaj dinner mein khana hai ya abhi bhi 'fridge ko admire kar rahe ho' mode on hai?",
"AG, SK, dinner complete hua ya aaj bhi 'hunger ki gaadi' chal rahi hai?",
   "SK aur AG, khana khaya ya sirf kahaniyan bana rahe ho?",
"Swati Kulshreshta and Anant Goyal, aaj dinner ke liye khana hai ya abhi bhi 'tasty talk show' chal raha hai?",
"AG aur SK, dinner update do – khana plate mein hai ya abhi bhi 'food delivery ka suspense' hai?",
    "DONE"
]


# File to store the current message index
INDEX_FILE = "message_index.txt"

def get_next_message_index():
    """Retrieve the next message index from the file."""
    try:
        # Read the current index from the file
        with open(INDEX_FILE, "r") as file:
            index = int(file.read().strip())
    except (FileNotFoundError, ValueError):
        # If the file doesn't exist or is invalid, start from the first message
        index = 0
    
    # Increment the index and loop back to 0 after reaching the end of the list
    next_index = (index + 1) % len(EVENING_MESSAGES)
    
    # Write the updated index back to the file
    with open(INDEX_FILE, "w") as file:
        file.write(str(next_index))
    
    return index

async def send_evening_reminder():
    """Send the evening medication reminder to the specified group chat."""
    # Validate bot token and chat ID
    if not BOT_TOKEN or not CHAT_ID:
        print("Error: Missing TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID.")
        return
    
    # Get the current message index and corresponding message
    message_index = get_next_message_index()
    message = EVENING_MESSAGES[message_index]
    
    # Initialize the bot and send the message
    bot = Bot(token=BOT_TOKEN)
    try:
        await bot.send_message(chat_id=CHAT_ID, text=message)
        print(f"Sent reminder: {message}")
    except Exception as e:
        print(f"Error sending reminder: {e}")

if __name__ == '__main__':
    asyncio.run(send_evening_reminder())
