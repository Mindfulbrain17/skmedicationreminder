# Medication Reminder Telegram Bot

This project is a **Telegram bot** that automatically sends daily medication reminders to a Telegram group at specific times. The bot ensures that reminders are sent on time without any manual intervention.

---

## **Features**
- Sends automated medication reminder messages to a **Telegram group**.
- Scheduled at three specific times daily:
  - **08:55 AM**  
  - **12:55 PM**  
  - **9:20 PM**
- Runs automatically using **GitHub Actions** as a cron job.
- Secure implementation using **GitHub Secrets** to hide sensitive data.

---

## **How It Works**
1. **Bot Creation**: A Telegram bot is created using [BotFather](https://core.telegram.org/bots#botfather), which provides a **Bot Token**.
2. **Group Setup**: Add the bot to a **Telegram group** where reminders are to be sent.
3. **Python Script**: A Python script is used to send predefined messages at specified times.
4. **Automation**: GitHub Actions is configured to run the script at the desired times using a **cron schedule**.
5. **Security**: Sensitive credentials like the Bot Token and Group Chat ID are stored securely using **GitHub Secrets**.

---

## **Prerequisites**
- A Telegram bot created via BotFather.
- A Telegram group with the bot added.
- A GitHub account for automation.

---

## **Setup Instructions**

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/your-username/medication-reminder-bot.git
cd medication-reminder-bot
```

### **Step 2: Create a Telegram Bot**
1. Open Telegram and search for `BotFather`.
2. Send `/newbot` to create a new bot.
3. Follow the instructions and copy the provided **Bot Token**.

### **Step 3: Add the Bot to a Group**
1. Create a new Telegram group.
2. Add the bot you created to this group.
3. Send a message in the group and note the **Chat ID** using tools like [getids bot](https://t.me/getidsbot).

### **Step 4: Store Secrets in GitHub**
1. Go to your GitHub repository.
2. Navigate to `Settings > Secrets and variables > Actions`.
3. Add the following secrets:
   - `TELEGRAM_BOT_TOKEN`: Your bot's token.
   - `TELEGRAM_CHAT_ID`: The group chat ID.

### **Step 5: Configure GitHub Actions**
The workflow file `medication_reminder.yml` is already configured. It looks like this:

```yaml
name: Medication Reminder Bot

on:
  schedule:
    - cron: '53 9 * * *'    # 10:00 AM (adjusted for delays)
    - cron: '48 12 * * *'   # 12:55 PM
    - cron: '13 21 * * *'   # 9:20 PM

jobs:
  send-reminder:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout repository
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install python-telegram-bot

    - name: Run Medication Reminder Bot
      env:
        TELEGRAM_BOT_TOKEN: ${{ secrets.TELEGRAM_BOT_TOKEN }}
        TELEGRAM_CHAT_ID: ${{ secrets.TELEGRAM_CHAT_ID }}
      run: python medication_reminder_bot.py
```

### **Step 6: Run the Bot**
- Push the code to your GitHub repository.
- GitHub Actions will automatically run at the specified times to send reminders.

---

## **Python Script**
Below is the main Python script (`medication_reminder_bot.py`) that sends messages:

```python
import os
import asyncio
from telegram import Bot

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
    try:
        await bot.send_message(chat_id=CHAT_ID, text=message)
        print(f"Sent reminder: {message}")
    except Exception as e:
        print(f"Error sending reminder: {e}")

async def main():
    # Initialize the Telegram bot
    bot = Bot(token=BOT_TOKEN)
    # Index-based message sending for different times
    current_hour = int(os.environ.get('HOUR_INDEX', 0))
    await send_medication_reminder(bot, REMINDER_MESSAGES[current_hour])

if __name__ == '__main__':
    asyncio.run(main())
```

---

## **Testing and Troubleshooting**
- Ensure the bot is added to the group and not blocked.
- Verify `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` are correct.
- Check GitHub Actions logs for errors.
- Adjust cron timing slightly ahead to mitigate delays in execution.

---

## **Future Improvements**
- Add support for custom reminder times.
- Log messages sent for tracking.
- Allow users to modify reminders via Telegram commands.

---

## **License**
This project is licensed under the MIT License.

---

## **Credits**
Developed with ❤️ by [Anant Goyal](https://github.com/Anant-Goyal).
