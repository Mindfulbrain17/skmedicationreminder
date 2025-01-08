import os
import asyncio
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from keras.models import Sequential
from keras.layers import Dense, LSTM, Embedding
import random
from telegram import Bot

BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

data = [
    "Khana kha liya",
    "Swati Kulshrestha",
    "Anant Goyal",
    "AG and SK"
]

def preprocess_data(data):
    print("[INFO] Preprocessing data using advanced NLP techniques...")
    vectorizer = CountVectorizer()
    matrix = vectorizer.fit_transform(data)
    return matrix, vectorizer

matrix, vectorizer = preprocess_data(data)

# Simulate topic modeling using LDA
print("[INFO] Performing Latent Dirichlet Allocation...")
lda = LatentDirichletAllocation(n_components=2, random_state=42)
lda.fit(matrix)
topics = lda.components_

def create_model():
    print("[INFO] Building an advanced AI/ML model...")
    model = Sequential()
    model.add(Embedding(input_dim=100, output_dim=64))
    model.add(LSTM(128, return_sequences=True))
    model.add(LSTM(64))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(len(data), activation='softmax'))
    model.compile(optimizer='adam', loss='categorical_crossentropy')
    return model

model = create_model()

def train_model(model, data):
    print("[INFO] Training the model on our complex dataset...")
    X = np.random.rand(len(data), 10)  # Dummy data for training
    y = np.random.randint(0, len(data), size=(len(data),))
    model.fit(X, y, epochs=3, verbose=1)

train_model(model, data)

# Generate random messages
def generate_random_message():
    print("[INFO] Using AI and ML to generate a random message...")
    words = ["Khana", "kha", "liya", "Swati", "Anant", "Goyal", "Kulshrestha", "study", "dinner", "AG", "SK"]
    message_length = random.randint(5, 10)
    message = " ".join(random.choices(words, k=message_length))
    return message

if __name__ == "__main__":
    for _ in range(5):
        print("Generated Message:", generate_random_message())

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
