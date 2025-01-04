# Medication Reminder Bot

This project is a highly customizable Telegram bot designed to send medication reminder messages to a group or individual at a specified time daily. It is automated using GitHub Actions and supports features such as cyclic message rotation and customizable message content.

## Key Features

### 1. **Daily Reminder System**
- Sends a single reminder message every day at a fixed time (8:55 PM IST / 3:25 PM UTC).
- Reminder time is managed via GitHub Actions' cron jobs.

### 2. **Rotating Messages System**
- The bot cycles through a predefined list of 15 messages.
- Messages are sent one by one each day.
- After completing the 15th message, the bot starts again from the first message, ensuring continuity.

### 3. **Customizable Messages**
- Users can easily modify the 15 predefined messages in the `EVENING_MESSAGES` list of the Python script.
- Each message is carefully crafted to ensure engagement and reminders.

### 4. **Fully Automated**
- The bot runs on GitHub Actions and does not require manual intervention once deployed.
- Automatically updates the `message_index.txt` file in the repository to keep track of the next message to be sent.

### 5. **Telegram API Integration**
- Uses the Telegram Bot API to send messages to a specified chat group or individual.
- Bot token and chat ID are securely managed using GitHub Secrets.

### 6. **Lightweight and Efficient**
- Minimal dependencies (`python-telegram-bot` library).
- Designed to be simple and highly maintainable.

## Setup Instructions

### Prerequisites
1. A Telegram bot token obtained from the [BotFather](https://core.telegram.org/bots#botfather).
2. The chat ID of the group or individual where the reminders will be sent.
3. A GitHub repository to host the project.

### Steps to Deploy

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/medication-reminder-bot.git
   cd medication-reminder-bot
   ```

2. **Modify the Message List**
   Update the `EVENING_MESSAGES` list in `medication_reminder_bot.py` with your custom messages.

3. **Add Secrets to GitHub**
   - Navigate to your repository on GitHub.
   - Go to **Settings > Secrets and variables > Actions > New repository secret**.
   - Add the following secrets:
     - `TELEGRAM_BOT_TOKEN`: Your Telegram bot token.
     - `TELEGRAM_CHAT_ID`: The chat ID of the recipient group or individual.

4. **Push the Code to GitHub**
   Commit and push the modified code to your GitHub repository.

5. **Set Up GitHub Actions Workflow**
   The workflow is already configured in `.github/workflows/medication_reminder.yml` to run daily at 8:55 PM IST (3:25 PM UTC).

### Project Files

- `medication_reminder_bot.py`: The main script for sending Telegram messages.
- `message_index.txt`: Keeps track of the last message sent (automatically updated by the script).
- `.github/workflows/medication_reminder.yml`: GitHub Actions workflow configuration.

## How It Works

1. **Message Sending Logic**
   - The bot reads the current `message_index` from `message_index.txt`.
   - Sends the message corresponding to that index from the `EVENING_MESSAGES` list.
   - Updates `message_index.txt` to the next index.

2. **Cyclic Messaging**
   - When the `message_index` exceeds the number of messages in `EVENING_MESSAGES`, it resets to `0`, ensuring the messages loop back to the beginning.

3. **GitHub Actions Automation**
   - The workflow runs the Python script daily at the scheduled time.
   - Ensures consistent message delivery without manual intervention.

## Example Messages
Here are some examples of the rotating evening messages:

- "X and Y, have you eaten dinner yet, or are you still scrolling through memes?"
- "X, did you remind Y to have dinner, or are you both skipping it again?"
- "X and Y, what’s cooking? Hopefully, not just excuses!"
- "Y, remind X to have dinner. It's a team effort!"

You can replace these with your own custom messages as per your needs.

## Future Improvements
- Add support for sending completely random messages from the list instead of cycling through them sequentially.
- Implement a web interface for managing messages and schedules.
- Enhance logging and monitoring capabilities for debugging and analytics.

## License
This project is open-source and available under the [MIT License](LICENSE).

---

## **Credits**
Developed with ❤️ by [Anant Goyal](https://github.com/Anant-Goyal).

For questions or suggestions, feel free to reach out to Anant Goyal, the mastermind behind this project!
