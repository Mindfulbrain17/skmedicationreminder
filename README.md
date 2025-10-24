# Medication Reminder Bot

This project is a Telegram bot that automatically sends daily medication reminders to a Telegram group at specific times. The bot ensures timely reminders without any manual intervention, leveraging a fully automated system powered by GitHub Actions.

---

## How the System Works

1. **Scheduling & Automation**
   - The bot is triggered daily by a GitHub Actions workflow (`.github/workflows/medication_reminder.yml`) at 8:55 PM IST (3:25 PM UTC).
   - No manual action is required once setup is complete.

2. **Message Selection**
   - The main script (`medication_reminder_bot.py`) maintains a list of 15 customizable messages (`EVENING_MESSAGES`).
   - The bot reads the current message index from `message_index.txt`.
   - Each day, it sends the message at the current index, then updates the index for the next run.
   - When all messages are sent, the index resets to zero, creating a continuous loop.

3. **Telegram API Integration**
   - Messages are sent directly to a Telegram group or individual using the Telegram Bot API.
   - Bot credentials (`TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID`) are securely stored as GitHub repository secrets.

---

## Project Files and Their Use Cases

| File                                       | Purpose & Use Case                                                                      |
|---------------------------------------------|----------------------------------------------------------------------------------------|
| `medication_reminder_bot.py`                | Main script. Reads message index, sends Telegram message, updates index for next run.   |
| `message_index.txt`                         | Stores the index of the last sent message. Ensures the correct message sequence daily.  |
| `.github/workflows/medication_reminder.yml` | GitHub Actions workflow configuration. Schedules and runs the bot script automatically. |

---

## Detailed Step-by-Step Workflow

1. **GitHub Actions starts the workflow at scheduled time.**
2. The workflow runs `medication_reminder_bot.py`.
3. The script:
    - Loads `EVENING_MESSAGES` (your reminder texts).
    - Reads `message_index.txt` to determine which message to send.
    - Sends the message via Telegram API using secrets for authentication.
    - Increments the index and saves it back to `message_index.txt`.
    - If index exceeds number of messages, resets to 0 for cyclic reminders.

---

## Setup Instructions

1. **Prerequisites**
    - Telegram bot token (from BotFather).
    - Chat ID for your group or self.
    - GitHub repository to host the code.

2. **Clone and Configure**
    ```bash
    git clone https://github.com/Mindfulbrain17/skmedicationreminder.git
    cd skmedicationreminder
    ```
    - Edit `EVENING_MESSAGES` in `medication_reminder_bot.py` for your custom reminders.

3. **Add GitHub Secrets**
    - Go to repository Settings > Secrets and variables > Actions > New repository secret.
    - Add:
        - `TELEGRAM_BOT_TOKEN`
        - `TELEGRAM_CHAT_ID`

4. **Push Code**
    - Commit and push your changes.

5. **Automation**
    - The workflow is ready to run daily as scheduled.

---

## Example Messages

Some of the rotating messages (customizable):
- "X and Y, have you eaten dinner yet, or are you still scrolling through memes?"
- "X, did you remind Y to have dinner, or are you both skipping it again?"
- "Y, remind X to have dinner. It's a team effort!"

---

## Minute-to-Minute Details

- **Fully Automated:** No manual intervention after setup.
- **Message Loop:** Ensures variety and continuity.
- **Easy Customization:** Just edit the message list in Python script.
- **Secure:** Credentials are managed via GitHub Secrets.
- **Efficient:** Minimal dependencies, fast execution, and easily maintainable.

---

## Future Improvements

- Option for random message selection.
- Web interface for editing messages/schedules.
- Enhanced logging and analytics.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

## Credits

Developed with ❤️ by [Anant Goyal](https://github.com/Anant-Goyal).
For questions or suggestions, feel free to reach out!
