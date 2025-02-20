import os
import asyncio
from telegram import Bot

# Retrieve bot token and chat ID from environment variables
BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

# Evening reminder messages (Random Generated Messages)
EVENING_MESSAGES = [
   "AG aur SK, khana plate mein tha ya sirf doston ke WhatsApp messages mein discuss ho raha tha?", 
   "AG aur SK, kya khana fridge mein dekhke sirf ‘Aaj mann nahi hai’ bol rahe ho?",  
   "AK, khana ho gaya ya SK ke saath discuss kar rahe ho ki aaj ka dinner kal kar lein?", 
"Anant Goyal aur Swati Kulshrestha, kya dinner decide ho gaya ya ab tak ‘Tu bata, tu bata’ chal raha hai?",  
   "SK aur AG, kya aaj bhi dinner ki jagah sirf chai aur biscuits pe guzara ho raha hai?",  
   "Swati Kulshrestha aur Anant Goyal, kya khana banana start kiya ya abhi bhi recipe dhoond rahe ho?",  
   "Swati Kulshrestha aur Anant Goyal, kya khana sirf doston ke Instagrams pe enjoy kar rahe ho ya khud bhi kuch banaya?",  
   "Swati aur Anant, kya aaj bhi dinner plan bas ‘Jo fridge mein milega wahi’ hai?",  
   "AG aur SK, kya khana kha liya ya sirf fridge ke saamne pose maar rahe ho?",  
   "Swati aur Anant, khana kha liya ya phir ‘Bas 10 minute aur’ chal raha hai?",  
   "Swati Kulshrestha aur Anant Goyal, kya aaj bhi khana sirf midnight snack ban ke raha gaya?", 
"Swati Goyal aur Anant Kulshrestha, kya khana sirf plate mein sajaya ya actually khaya bhi?",
   "Swati aur Anant, kya dinner decide ho gaya ya ‘Tu bata, tu bata’ chal raha hai?",  
   "Anant aur Swati, kya dinner ke naam pe sirf chai aur biscuits pe zinda ho?",  
   "Swati Kulshrestha aur Anant Goyal, kya khana banana start kiya ya abhi bhi recipe dhoond rahe ho?",  
   "AK aur SK, dinner ho gaya ya abhi bhi ‘Kuch light kha lete hain’ mood mein ho?", 
   "Swati aur Anant, khana kha liya ya firse ‘Bas 5 minute aur’ chal raha hai?",  
   "Anant Kulshrestha aur Swati Goyal, kya aaj bhi khana dekh ke ‘Kal se pakka diet’ wala promise kiya hai?",  
"Swati aur Anant, khana kha liya ya phir ‘Biryani ka mann ho raha hai’ soch rahe ho?",
   "AG aur SK, kya khana khaya ya sirf water therapy chal rahi hai?",  
"Swati Goyal aur Anant Kulshrestha, kya khana kha liya ya phir fridge ke samne deep thinking chal rahi hai?",  
"AK aur SG, kya plate bhar ke khaya ya sirf photo kheech ke social media pe daal diya?",  
"Anant Goyal aur Swati Kulshrestha, kya dinner ho gaya ya ‘Biryani ka mood ho raha hai’ wali dilemma chal rahi hai?",  
"AG aur SK, khana kha liya ya abhi bhi Swiggy pe discount dhoond rahe ho?",  
"Swati aur Anant, kya aaj bhi dinner ‘Bas ek bite aur’ pe chal raha hai?",  
"SG aur AK, dinner ho gaya ya ‘Main khana banaun, tu saaf karega’ wali deal ab tak pending hai?",  
"SK aur AG, kya dinner ho gaya ya abhi bhi fridge ke andar ka view analyze ho raha hai?",  
"Swati aur Anant, kya aaj bhi khana banane se zyada order karne pe discussion hua?",  
"AG aur SG, dinner ho gaya ya abhi bhi ‘Mann nahi kar raha’ wala excuse chal raha hai?",  
"Anant aur Swati, kya khana plate tak aaya ya sirf dimaag mein soch rahe ho?",  
"Swati Kulshrestha aur Anant Goyal, kya khana banana start kiya ya abhi bhi recipe dhoond rahe ho?",  
"AK aur SK, dinner ho gaya ya abhi bhi ‘Kuch light kha lete hain’ mood mein ho?",  
"Swati aur Anant, kya dinner decide ho gaya ya ‘Tu bata, tu bata’ ab tak chal raha hai?",  
"Swati aur Anant, kya aaj bhi dinner ka plan ‘Dekh lenge’ hai?",  
"Anant Goyal aur Swati Kulshrestha, kya dinner ho gaya ya ‘Bas ek aur episode dekh ke’ mood mein ho?",  
"Swati Goyal aur Anant Kulshrestha, khana kha liya ya sirf ‘Aaj toh fasting hai’ wali baat chal rahi hai?",  
"SG aur AK, kya khana kha liya ya sirf YouTube pe cooking videos dekh ke pet bhar raha hai?",  
"Anant aur Swati, kya dinner ho gaya ya ‘Kuch accha khane ka mann hai’ wali feeling aa rahi hai?",  
"AG aur SK, kya aaj bhi dinner plan bas ‘Jo fridge mein milega wahi’ hai?",  
"Swati Kulshrestha aur Anant Goyal, kya aaj bhi khana sirf midnight snack ban ke raha gaya?",  
"AG aur SG, dinner ho gaya ya ‘Aaj sirf maggi’ plan hai?",  
"Anant aur Swati, kya khana kha liya ya abhi bhi ‘Kuch order karein?’ discussion ho raha hai?",  
"SK aur AK, kya dinner ho gaya ya abhi bhi ‘Aaj mann nahi hai’ excuse chal raha hai?",  
"Swati aur Anant, kya aaj ka dinner sirf sochne tak hi raha?",  
"AG aur SK, kya dinner decide karna aaj bhi mission impossible lag raha hai?",    
"SG aur AK, kya aaj bhi ‘Biryani ya pizza?’ discussion 2 ghante chala?",  
"Anant aur Swati, kya dinner ka sirf photo liya ya actually kuch khaya bhi?",  
"AG aur SK, kya aaj bhi dinner ‘Jo dikh gaya wahi best hai’ pe chal raha hai?",  
"Swati aur Anant, kya aaj bhi dinner ‘Bhook nahi hai’ wali feeling se chalu hua?",  
"AK aur SG, kya dinner decide karne mein itna time laga ki khud bhook mar gayi?",  
"Anant aur Swati, kya dinner ke naam pe sirf chai aur biscuits pe zinda ho?",  
"AG aur SK, kya aaj bhi dinner discuss karte karte bhook hi chali gayi?",  
"Swati Kulshrestha aur Anant Goyal, kya dinner decide ho gaya ya ab tak ‘Tu bata, tu bata’ chal raha hai?",  
"SK aur AG, kya aaj bhi dinner banana chhoda aur ‘Koi simple sa bana lo’ mode on hai?",  
"Swati aur Anant, kya aaj bhi dinner ka sirf plan bana ya actually khana bhi khaya?",  
"AG aur SK, kya khana khaya ya sirf paani pe chal raha hai?",  
"Swati aur Anant, kya dinner ki recipe itni lambi thi ki bhook khatam ho gayi?",  
"AK aur SG, kya aaj bhi dinner ka plan ‘Biryani khate hain’ pe khatam ho gaya?",  
"Anant aur Swati, kya dinner sirf doston ke Instagrams pe enjoy kar rahe ho ya khud bhi kuch banaya?",  
"SG aur AK, kya khana kha liya ya abhi bhi ‘Bas 10 minute aur’ mood mein ho?",  
"AG aur SK, kya dinner ho gaya ya ‘Aaj fast kar raha hoon’ excuse chal raha hai?",  
"Swati aur Anant, kya dinner bas ‘Kal se proper diet’ pe chala gaya?",  
"AK aur SK, kya dinner ho gaya ya abhi bhi ‘Bhook nahi hai’ ka natak chal raha hai?",  
    "AG aur SK, kya khana khaya ya fir fridge ko motivation speech de rahe ho?",  
"Swati aur Anant, dinner ho gaya ya abhi bhi ‘kuch light sa kha lete hain’ soch rahe ho?",  
"Anant Goyal aur Swati Kulshrestha, khana plate mein hai ya sirf dimaag mein?",  
"AG aur SK, kya aaj bhi dinner ka plan sirf ‘sochne’ tak limited hai?",   
"Swati aur Anant, khana plate se uda diya ya actually kha bhi liya?",  
"AG aur SK, kya tum dono ke dinner plans mein ek rule hai—'Mera khana, tera khana hai'?",  
"AG aur SK, khana kha liya ya sirf kahaniyan digest ho rahi hain?",  
"Swati Kulshrestha aur Anant Goyal, khana ho gaya ya abhi bhi Swiggy ka discount code dhoond rahe ho?",  
"AG aur SK, kya aaj dinner ki jagah sirf memes consume ho rahe hain?",  
"Swati aur Anant, kya aaj bhi dinner ka menu 'Jo mil gaya wahi best hai' hai?",  
"AG aur SK, khana kha liya ya fridge ke andar ka view analyze kar rahe ho?",  
"Swati aur Anant, dinner ho gaya ya bas good vibes aur chai pe chal raha hai?",  
"Anant Goyal aur Swati Kulshrestha, kya aaj bhi dinner ‘kal se pakka’ wale plans mein hai?",  
"AG aur SK, dinner ho gaya ya firse snacks pe compromise ho raha hai?", 
"AG aur SK, kya dinner ka matlab aaj bhi sirf chai aur biscuits hai?",  
"Swati aur Anant, khana kha liya ya phir fridge ke samne bas ‘Soch rahe hain’ mode on hai?",  
"AG aur SK, khana plate mein tha ya sirf doston ke WhatsApp messages mein discuss ho raha tha?",  
"Swati aur Anant, kya dinner decide ho gaya ya ‘Tu bata, tu bata’ chal raha hai?",  
"AG aur SK, kya khana fridge mein sirf storage ke liye rakha hai ya actually khana bhi hai?",  
"Swati aur Anant, dinner ho gaya ya fir 'Kuch accha khaane ka mann ho raha hai' wali feeling aa rahi hai?",  
"AG aur SK, kya aaj bhi sirf ‘Kuch halka phulka kha lete hain’ plan hai?",  
"Swati aur Anant, khana khaya ya sirf food blogs scroll karte reh gaye?",  
"AG aur SK, dinner ho gaya ya ‘Pizza order karein?’ discussion ab tak chal raha hai?",  
"Swati aur Anant, kya khana microwave mein garam karte karte thanda kar diya?",  
"AG aur SK, dinner ho gaya ya sirf ‘Aaj diet shuru karni hai’ discuss kar rahe ho?",  
"Swati aur Anant, khana ho gaya ya fridge ko sirf emotional support ke liye khol rahe ho?",  
"AG aur SK, kya dinner ke naam pe sirf energy drink pe survive kar rahe ho?",  
"AG aur SK, dinner ho gaya ya abhi bhi ‘Main khana banata hoon, tu saaf karega’ wali deal chal rahi hai?",  
"Swati aur Anant, kya aaj dinner ka bhi vlog banane ka plan hai?",  
"Swati aur Anant, dinner ho gaya ya ‘Aaj fast kar raha hoon’ excuse chal raha hai?",  
"AG aur SK, kya dinner sirf ‘Jo bacha hai wahi khana padega’ mode pe hai?",  
"Swati aur Anant, kya khana banana start kiya ya abhi bhi recipes dhoond rahe ho?",  
"AG aur SK, dinner ho gaya ya ‘Bhook toh lagi hai par uthne ka mann nahi hai’ mode on hai?",  
"Swati aur Anant, kya khana sirf doston ke Instagrams pe enjoy kar rahe ho ya khud bhi kuch banaya?",  
"AG aur SK, khana ho gaya ya ‘Abhi tak decide nahi kiya’ zone mein ho?",  
"Swati aur Anant, kya aaj bhi dinner ke naam pe sirf Maggi ka plan hai?",  
"AG aur SK, kya khana kha liya ya fridge ke samne sirf deep thoughts le rahe ho?",  
"Swati aur Anant, dinner ho gaya ya sirf online food delivery apps explore kar rahe ho?",  
"AG aur SK, kya aaj bhi sirf ‘Bread butter se kaam chala lete hain’ plan hai?",  
"Swati aur Anant, khana kha liya ya phirse ‘Chal chai peete hain’ mood on hai?",  
"AG aur SK, kya dinner ka sirf photo liya ya actually khaya bhi?",  
"Swati aur Anant, kya aaj ka dinner bas ‘Kal se proper diet’ pe chala gaya?",  
"AG aur SK, kya khana ho gaya ya abhi bhi ‘Bhook nahi hai’ jhooth chal raha hai?",  
"Swati aur Anant, dinner ho gaya ya ‘Bas ek aur episode dekh ke’ wala mood hai?",  

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
