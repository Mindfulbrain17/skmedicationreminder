import os
import asyncio
from telegram import Bot

# Retrieve bot token and chat ID from environment variables
BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

# Evening reminder messages (15 predefined messages)
EVENING_MESSAGES = [
    "AG aur SK, khana khaoge ya sirf reels dekh kar bhook mitane ka plan hai?",
    "Khana kha liya kya, Swati Kulshrestha & Anant Goyal?",
    "Anant Kulshrestha aur Swati Goyal, khana khaya ya phir se busy ho?",
    "AG & SK, khana kaisa tha ya abhi tak nahi khaya?",
    "Swati Goyal, tumne khana khaya? AG ka pata hai?",
    "Anant Goyal and Swati Kulshrestha, kha liya khana ya sirf baatein chal rahi hain?",
    "Swati Kulshrestha aur Anant Goyal, kya aap log abhi bhi bhookhe hain?",
    "Swati Goyal aur Anant Kulshrestha, kya khana kha rahe ho ya photos click kar rahe ho Instagram ke liye?",
    "SK aur AG, khana plate se uda diya ya actually kha bhi liya?",
    "AG, tumne khana kha liya ya SK ka 'mein diet pe hoon' sunke skip kar diya?",
    "Anant Goyal & Swati Goyal, kya khana skip kar diya fir se?",
    "AG, khana kha liya kya? Aur SK, tumhe bhi yaad dilana padega?",
    "Kya AG aur SK ne khana khaya ya fir snacks pe guzara kar rahe ho?",
    "Swati Kulshrestha aur Anant Kulshrestha, ab to khana kha lo!",
    "SK aur AG, khana khaya ya sirf kahaniyan bana rahe ho?",
    "Swati Goyal, tumhara khana ho gaya? AG ka pata nahi, shayad busy hoga!",
    "Swati Kulshrestha aur Anant Goyal, khana kha liya kya ya abhi bhi soch rahe ho Swiggy ya Zomato?",
    "AG aur SK, khaana kha liya ya abhi bhi 'bas 2 minute' noodles ban rahe hain?",
    "Swati Goyal aur Anant Kulshrestha, tum dono khana khaoge ya bhookh ki ladayi mein jeet milegi?",
    "AG aur SK, kya khana kha liya ya abhi bhi fridge ke saamne meditation kar rahe ho?",
    "Khana kha liya kya, AG aur SK, ya abhi bhi baatein hi digest ho rahi hain?",
    "Swati Kulshrestha aur Anant Goyal, khana khaya ya dieting ka naya excuse hai?",
    "AG aur SK, kya khana plate mein rakha selfie le rahe ho ya kha bhi rahe ho?",
    "Swati Goyal aur Anant Kulshrestha, kya tum dono khana khaoge ya Wi-Fi pe zinda ho?",
    "AG, khana kha liya? SK ko bhi bolna, chat chutney ka option nahi hai dinner mein!",
    "Anant Kulshrestha aur Swati Goyal, kya khana aaj bhi pending hai?"
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

    # Increment the index and loop back to 0 after 15 messages
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
