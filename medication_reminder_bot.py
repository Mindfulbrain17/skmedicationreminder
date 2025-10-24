import os
import asyncio
from telegram import Bot

# Retrieve bot token and chat ID from environment variables
BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

# Evening reminder messages (Random Generated Messages)
EVENING_MESSAGES = [
   "Swati aur Anant, khana ready hai ya abhi bhi 'soch rahe ho kya banaye' mode on hai?",
"AG aur SK, dinner ho gaya ya abhi bhi 'kitchen tour' chal raha hai?",
"Swati Kulshreshta and Anant Goyal, khana kha liya ya fridge inspection baki hai?",
"AG, SK, dinner complete ya abhi bhi 'taste test trial' chal raha hai?",
"Swati aur Anant, pet bhar gaya kya ya aur ek round soch rahe ho?",
   "SK aur AG, dinner complete hua ya abhi bhi depression ke saath cutlery polish kar rahe ho?",
"Swati Kulshreshta and Anant Goyal, khana khaya ya abhi bhi utensil ke reflection mein apna purpose dhoond rahe ho?",
"SK aur AG, khana khatam hua ya abhi bhi spoon aur fork fight kar rahe ho?",
"Swati Kulshreshta and Anant Goyal, khana plate mein aa gaya ya abhi bhi 'order placed' ka status hai?",
"AG aur SK, pet bhar gaya ya abhi bhi 'thoda aur' bol kar baith gaye ho?",
"Swati aur Anant, dinner mode off hua kya ya abhi bhi ‘ek bite aur’ ka plan hai?",
"SK aur AG, khana khaya ya abhi bhi menu scroll ho raha hai?",
   "AG, SK, khana khatam kiya ya abhi bhi 'aakhri bite ke liye competition' chal raha hai?",
   "SK aur AG, dinner finish hua ya abhi bhi 'last supper ki tasveer bana rahe ho'?",
"Swati Kulshreshta and Anant Goyal, dinner complete hua ya abhi bhi taste buds meeting chal rahi hai?",
"AG aur SK, khana finish kar liya ya abhi bhi ‘khaane ki kahani’ likh rahe ho?",
"Swati aur Anant, kitchen close hua kya ya abhi bhi ‘chef ke experiment’ chal rahe hain?",
"SK aur AG, dinner ho gaya ya abhi bhi spoon warm-up kar raha hai?",
"Swati Kulshreshta and Anant Goyal, khana kha liya ya abhi bhi ‘food comedy show’ dekh rahe ho?",
"AG aur SK, bowl khali hua kya ya abhi bhi ‘last bite ka drama’ chal raha hai?",
"Swati aur Anant, dinner done ya abhi bhi ‘plate decoration competition’ chal raha hai?",
"SK aur AG, khana kha liya ya abhi bhi ‘waiter bulao’ wala mood on hai?",
   "Swati aur Anant, khana khaya ya abhi bhi life decisions microwave mein garam kar rahe ho?",
   "AG aur SK, dinner ho gaya ya abhi bhi guilt aur carbs dono digest nahi ho rahe?",
"Swati Kulshreshta and Anant Goyal, dinner ka chapter close hua kya ya abhi bhi rehearse kar rahe ho?",
"AG aur SK, dinner khatam hua ya abhi bhi ‘kitchen adventure part-2’ pending hai?",
"Swati aur Anant, dinner ready ya 'fork drop suspense' chal raha hai?",
"AG, SK, khana khaya ya 'bite hesitation game' on?",
"SK aur AG, plates full hain ya 'hunger hide-and-seek' khel rahe ho?",
"Swati Kulshreshta and Anant Goyal, pet pooja time ya 'snack sabotage' mode?",
"AG aur SK, dinner done ya 'chew slowly challenge' fail?",
   "Swati aur Anant, dinner complete ya zindagi ka plot twist abhi bhi uncooked hai?",
"SK aur AG, khana khatam hua ya abhi bhi 'Bhagwan ne bhi mujhe garnish kiya hota' soch rahe ho?",
"Swati Kulshreshta and Anant Goyal, khana khata waqt realise hua – taste life jaisa hai, thoda burnt par fir bhi chalega."
"Swati aur Anant, khaya ya abhi 'flavor flirt' kar rahe ho?",
"AG, SK, table par attack ya 'napkin ninja moves' practice?",
"SK aur AG, bhookh bhagi ya 'leftover love story' likh rahe ho?",
"Swati Kulshreshta and Anant Goyal, dinner success ya 'spice surprise' twist?",
"AG aur SK, khana tasty tha ya 'taste test tantrum'?",
   "Swati aur Anant, khana khaya ya abhi bhi 'diet plan fail' hone ka intezaar hai?",
"AG aur SK, dinner ho gaya ya abhi bhi 'fridge mein chhupa khana' dhoond rahe ho?",
"Swati Kulshreshta and Anant Goyal, pet bhar gaya ya abhi bhi 'empty plate ka sapna' dekh rahe ho?",
"AG, SK, khana khatam kiya ya abhi bhi 'khaate hi rehne wale' team mein ho?",
"Swati aur Anant, dinner complete ya abhi bhi 'TV remote se zyada khane mein interest' hai?",
"SK aur AG, khana kha liya ya abhi bhi 'delivery boy se speed contest' mein lage ho?",
"Swati Kulshreshta and Anant Goyal, khana khaya ya abhi bhi 'kitchen inspector ke wait' mein ho?",
"AG aur SK, pet bhar gaya ya abhi bhi 'extra plate ke liye fake fight' kar rahe ho?",
"Swati aur Anant, dinner kar liya ya abhi bhi 'iske baad bhi bhook lagi hai' mode mein ho?",
"SK aur AG, khana khatam kiya ya abhi bhi 'bina khaye TV serial dekhne ka maza le rahe ho?",
"Swati aur Anant, plates clean ya 'dish dash drama'?",
"AG, SK, pet happy ya 'midnight munch plot'?",
"SK aur AG, dinner wrap ya 'chai chase' next?",
"Swati Kulshreshta and Anant Goyal, khaya ya 'foodie fib'?",
"AG aur SK, table time over ya 'burp broadcast'?",
   "Swati aur Anant, khana serve ho gaya ya abhi bhi 'menu engineering' chal raha hai?",
"AG, SK, dinner ready hai ya 'culinary suspense thriller' ke climax ka wait hai?",
"Swati Kulshreshta and Anant Goyal, table par khana hai ya abhi bhi 'recipe plot twist' aa gaya?",
"AG aur SK, pet bhar gaya ya abhi bhi 'taste testing marathon' chal raha hai?",
"Swati aur Anant, khana khaya ya abhi bhi 'food photography film festival' mein busy ho?",
"SK aur AG, dinner ka chapter close hua ya 'chef’s emotional saga' continue hai?",
"Swati Kulshreshta and Anant Goyal, khaana khatam hua ya abhi bhi 'recipe revision 3.0' chal raha hai?",
"AG aur SK, table pe dinner hai ya abhi bhi 'fridge contemplation' mood on hai?",
"Swati aur Anant, kitchen cool down mode mein ho ya abhi bhi 'culinary experiment season finale' shoot ho raha hai?",
"SK aur AG, khaana khatam kara ya abhi bhi 'taste buds committee meeting' chal raha hai?",
"Swati Kulshreshta and Anant Goyal, khana plate mein hai ya abhi bhi 'menu finalization debate' pending hai?",
"AG aur SK, dinner kar liya ya abhi bhi 'flavor calibration lab test' chal raha hai?",
"Swati aur Anant, pet bhar gaya ya abhi bhi 'food nostalgia archives' browse kar rahe ho?",
"SK aur AG, khaana finished hai ya abhi bhi 'culinary research internship' jaari hai?",
"Swati Kulshreshta and Anant Goyal, khaana khatam hua ya abhi bhi 'dinner time chronicles' likh rahe ho?",
"AG aur SK, khana khatam ya abhi bhi 'chef’s reality show' ke judges bane baithe ho?",
"Swati aur Anant, dinner ho gaya ya abhi bhi 'spoon vs fork showdown' chal raha hai?",
"SK aur AG, dinner complete hua ya abhi bhi 'taste recertification exam' dene wale ho?",
"Swati Kulshreshta and Anant Goyal, khana khatam hua ya abhi bhi 'culinary nostalgia season 2' record ho raha hai?",
"AG aur SK, khana khaya ya abhi bhi 'kitchen post-credit scene' ka wait kar rahe ho? :)",
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
