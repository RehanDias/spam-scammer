
# SPAM scammer using making request 📩

This project consists of two implementations, one in Python (`app.py`) and the other in NodeJs (`app.js`), for sending messages to a Telegram chat using the Telegram Bot API, to spamming API scammer.

## Python Implementation (`app.py`) 🐍

### Configuration Variables 🛠️
- `botToken`: 🤖 Token for the Telegram bot.
- `chatId`: 💬 ID of the chat where messages will be sent.
- `message`: 📝 The message to be sent.
- `interval`: ⏱️ Time interval in seconds between each message sent.
- `requestRetryInterval`: ⏳ Time interval in seconds before retrying after encountering a 429 HTTP error (rate limit exceeded).
- `numberOfRequests`: 📈 Total number of requests to be sent.

### Usage 🚀
1. Replace the configuration variables (`botToken`, `chatId`, `message`, etc.) with your own values.
2. Install the required dependencies:
   ```bash
   pip install urllib3
   ```
3. Run the `app.py` file:
   ```bash
   python app.py
   ```

### Installation Steps (Python) 🛠️
- **Step 1:** Clone the repository:
  ```bash
  git clone https://github.com/your-username/telegram-bot-message-sender.git
  cd telegram-bot-message-sender
  ```
- **Step 2:** Install dependencies:
  ```bash
  pip install urllib3
  ```
- **Step 3:** Replace the configuration variables in `app.py` with your own values.
- **Step 4:** Run the Python script:
  ```bash
  python app.py
  ```

## NodeJs Implementation (`app.js`) 🟢

### Configuration Variables 🛠️
- `botToken`: 🤖 Token for the Telegram bot.
- `chatId`: 💬 ID of the chat where messages will be sent.
- `message`: 📝 The message to be sent.
- `interval`: ⏱️ Time interval in milliseconds between each message sent.
- `requestRetryInterval`: ⏳ Time interval in milliseconds before retrying after encountering a 429 HTTP error (rate limit exceeded).
- `numberOfRequests`: 📈 Total number of requests to be sent.

### Usage 🚀
1. Replace the configuration variables (`botToken`, `chatId`, `message`, etc.) with your own values.
2. Install the required dependencies:
   ```bash
   npm install axios
   ```
3. Run the `app.js` file:
   ```bash
   npm start
   ```

### Installation Steps (NodeJs) 🟢
- **Step 1:** Clone the repository:
  ```bash
  git clone https://github.com/your-username/telegram-bot-message-sender.git
  cd telegram-bot-message-sender
  ```
- **Step 2:** Install dependencies:
  ```bash
  npm install axios
  ```
- **Step 3:** Replace the configuration variables in `app.js` with your own values.
- **Step 4:** Run the NodeJs file:
  ```bash
  npm start
  ```

## Dependencies 📦
- Python Implementation:
  - `urllib`
  - `json`
  - `time`
- NodeJs Implementation:
  - `axios`

## Note 📝
Ensure that you have obtained the bot token and chat ID from Telegram and replaced them in the configuration variables before running the scripts.
