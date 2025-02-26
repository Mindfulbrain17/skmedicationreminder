import os
import asyncio
from telegram import Bot

# Retrieve bot token and chat ID from environment variables
BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

# Evening reminder messages (Random Generated Messages)
EVENING_MESSAGES = [
   "AG aur SK, dinner ho gaya ya ‘Aaj sirf maggi’ plan hai?",  
"AG aur SK, kya khana fridge mein dekh ke 'Aaj mann nahi hai' bol rahe ho?"
"SK aur AG, khana khaya ya sirf kahaniyan bana rahe ho?"
"Swati Kulshreshta and Anant Goyal, dinner ka status update do – kha liya ya sirf Insta selfies?"
"AG aur SK, kya khana plate mein aaya ya abhi bhi 'microwave marathons' chal rahe hain?"
"Swati aur Anant, aaj dinner mein khana hai ya phir 'Swiggy ke deals' ka naya twist?"
"AG, SK, khana kha liya ya abhi bhi 'order cancel' ka button dabaye hue ho?"
"Swati Kulshreshta and Anant Goyal, dinner complete hua ya abhi bhi fridge ke saath flirting chal rahi hai?"
"AG aur SK, aaj khana plate mein hai ya sirf 'food delivery ka pyaar' chalu hai?"
"Swati aur Anant, khana kha liya ya phir Swiggy-Zomato ke beech decision pending hai?"
"AG aur SK, dinner ka plan set hai ya abhi bhi 'maggi ke aashiq' ho?"
"Swati Kulshreshta and Anant Goyal, dinner ko leke kya agenda hai – khana khaoge ya TV remote chhodega?"
"AG aur SK, kya khana aaj bhi fridge ke saath flirt kar raha hai ya aap dono ne usse adopt kar liya?"
"Swati aur Anant, dinner ka scene hai ya abhi bhi 'leftover' ka plan hai?"
"AG, SK, khana khaya ya bas fridge ke magnets ko admire kiya?"
"Swati Kulshreshta and Anant Goyal, dinner ho gaya ya abhi bhi 'chef mode on' mein ho?"
"AG aur SK, aaj dinner mein khana hai ya sirf recipe books ka collection ban raha hai?"
"Swati aur Anant, kya aap log dinner ke liye cooking show dekh rahe ho ya khana bana rahe ho?"
"AG, SK, dinner complete hua ya aaj bhi 'snack time' ka extension chal raha hai?"
"Swati Kulshreshta and Anant Goyal, khana kha liya ya abhi bhi microwave se battle kar rahe ho?"
"AG aur SK, dinner plan clear hai ya abhi bhi 'delivery guy ke intezaar mein' ho?"
"Swati aur Anant, dinner ka progress report do – khana plate mein aaya ya abhi bhi in queue hai?"
"AG, SK, aaj dinner mein khana hai ya 'pyaar ka tarka' sirf conversation mein hai?"
"Swati Kulshreshta and Anant Goyal, dinner pe khana hai ya abhi bhi 'zero calorie' ka excuse chal raha hai?"
"AG aur SK, kya dinner ke liye khana hai ya 'order tracking app' hi dekh rahe ho?"
"Swati aur Anant, dinner ka naya twist hai – khana real hai ya just a delivery tracker?"
"AG, SK, dinner table ready hai ya abhi bhi 'kitchen sink drama' chal raha hai?"
"Swati Kulshreshta and Anant Goyal, dinner mein khana hai ya aap log 'dieting season' mein phase gaye ho?"
"AG aur SK, khana kha liya ya abhi bhi 'tiffin service' ki galiyon mein ghoom rahe ho?"
"Swati aur Anant, dinner pe khana hai ya abhi bhi 'recipe remix' soch rahe ho?"
    "Swati Kulshreshta and Anant Goyal, khana kha liya kya dono ne?"
"AG, SK, dinner complete hai ya aaj bhi 'snackathon' ka plan hai?"
"Swati Kulshreshta and Anant Goyal, kya dinner pe khana serve hua ya abhi bhi 'kitchen chaos' hai?"
"AG aur SK, dinner mein khana aaya ya abhi bhi 'cooking challenge' ka tension hai?"
"Swati aur Anant, aaj dinner pe khana hai ya sirf 'selfie mode on' hai?"
"AG, SK, aaj dinner plan mein khana hai ya sirf 'hunger ki baatein' chal rahi hain?"
"Swati Kulshreshta and Anant Goyal, dinner ho gaya ya abhi bhi 'order in process' ka suspense hai?"
"AG aur SK, dinner table par khana hai ya abhi bhi 'food festival in progress' ka wait hai?"
"Swati aur Anant, kya aaj dinner mein khana hai ya abhi bhi 'kitchen ke muse' ban rahe ho?"
"AG, SK, dinner complete hua ya aaj bhi 'gastronomy experiment' chal raha hai?"
"Swati Kulshreshta and Anant Goyal, khana plate mein hai ya abhi bhi 'culinary adventure' ka episode chal raha hai?"
"AG aur SK, dinner ka scene hai ya aaj bhi 'leftover treasure hunt' hai?"
"Swati aur Anant, aaj dinner pe khana hai ya sirf 'online food reviews' dekh rahe ho?"
"AG, SK, dinner ka update do – khana kha liya ya abhi bhi 'kitchen me baatein' chal rahi hain?"
"Swati Kulshreshta and Anant Goyal, aaj dinner mein khana hai ya abhi bhi 'food order pending' ka status hai?"
"AG aur SK, dinner pe khana aaya ya abhi bhi 'snack mode on' ka option hai?"
"Swati aur Anant, dinner complete hua ya abhi bhi 'kitchen ki kahaniyan' likh rahe ho?"
"AG, SK, khana kha liya ya abhi bhi 'cooking marathon' chal raha hai?"
"Swati Kulshreshta and Anant Goyal, dinner ka plan clear hai ya abhi bhi 'food delivery saga' chal raha hai?"
"AG aur SK, dinner table par khana hai ya abhi bhi 'order waiting game' chal raha hai?"
"Swati aur Anant, aaj dinner mein khana hai ya abhi bhi 'fridge ko admire kar rahe ho' mode on hai?"
"AG, SK, dinner complete hua ya aaj bhi 'hunger ki gaadi' chal rahi hai?"
"Swati Kulshreshta and Anant Goyal, aaj dinner ke liye khana hai ya abhi bhi 'tasty talk show' chal raha hai?"
"AG aur SK, dinner update do – khana plate mein hai ya abhi bhi 'food delivery ka suspense' hai?"
    "DONE",
     "Swati Kulshrestha aur Anant Goyal, dinner ho gaya ya abhi bhi WhatsApp pe memes digest kar rahe ho?",  
       "Anant Goyal & Swati Goyal, kya khana skip kar diya fir se?",
     "Kyo AG aur SG tum logo ne khana khaya ya fir snacks pe guzara kar rahe ho?",
    "SK aur AG, khana khaya ya sirf kahaniyan bana rahe ho?",
    "Swati Kulshrestha aur Anant Goyal, khana kha liya kya ya abhi bhi soch rahe ho Swiggy ya Zomato?",
    "Swati Kulshrestha aur Anant Goyal, khana khaya ya dieting ka naya excuse hai?",
    "Swati Goyal aur Anant Kulshrestha, kya tum dono khana khaoge ya Wi-Fi pe zinda ho?",
    "AG, khana kha liya? SK ko bhi bolna, chat chutney ka option nahi hai dinner mein!",
     "Khana kha liya kya, AG aur SK, ya abhi bhi baatein hi digest ho rahi hain?",
    "AK aur SK, kya khana plate mein rakha selfie le rahe ho ya kha bhi rahe ho?",
    "Anant Goyal and Swati Kulshrestha, kha liya khana ya sirf baatein chal rahi hain?",    
 "AG, tumne khana kha liya ya SK ka 'mein diet pe hoon' sunke skip kar diya?",
  "AG aur SK, kya tum dono ke dinner plans mein ek rule hai—'Mera khana, tera khana hai'?",
      "AG aur SK, kya khana kha liya ya abhi bhi fridge ke saamne meditation kar rahe ho?",
    "Swati aur Anant, khana plate se uda diya ya actually kha bhi liya?",
  "Kyo AG aur SG tum logo ne khana khaya ya fir snacks pe guzara kar rahe ho?",
  "Anant Goyal and Swati Kulshrestha, kha liya khana ya sirf baatein chal rahi hain?",
  "AG aur SK, khaana kha liya ya abhi bhi 'bas 2 minute' noodles ban rahe hain?",
    "AG, tumne khana kha liya ya SK ka 'mein diet pe hoon' sunke skip kar diya?",
    "Swati aur Anant, kya khana khaoge ya ek doosre ki shakal dekh kar hi 'delicious' feel kar rahe ho?",
    "Anant Goyal & Swati Goyal, kya khana aaj bhi tumhari padai ki tarah pending hai ?"
    "AG aur SK, khana khaoge ya sirf reels dekh kar bhook mitane ka plan hai?",
    "AK aur SK, kya notes ke beech khana rakha hai ya khana ke beech notes ban rahe hain? ",
    "Anant, tumhare khane ka plan bhi tumhare naam ki tarah endless hai? Swati toh 15th nakshatra ki tarah bas dekh rahi hai!",
    "Swati, tum khana kha rahi ho ya Goddess Saraswati ki tarah sirf knowledge share kar ke Anant ka patience infinite bana rahi ho ",
     "Swati Goyal aur Anant Kulshrestha, tum dono khana khaoge ya bhookh ki ladayi mein jeet milegi?",
     "Swati Kulshrestha aur Anant Kulshrestha, ab to khana kha lo!",
"Swati Goyal aur Anant Kulshrestha, kya khana kha rahe ho ya photos click kar rahe ho Instagram Par?"
  "AG, khana kha liya kya? Aur SK, tumhe bhi yaad dilana padega?",
 "Swati Goyal, tumhara khana ho gaya? AG ka pata nahi, shayad busy hoga!",
 "Swati Kulshrestha aur Anant Goyal, khana kha liya kya ya abhi bhi soch rahe ho Swiggy ya Zomato?"
"Swati, tumhare khane ki speed dekh kar lagta hai ki Goddess Saraswati bhi soch rahi hongi, 'Yeh to eternally slow hai!' Meanwhile, Anant ab tak endless wait kar raha hai!"
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
