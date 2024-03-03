import json
import time
import urllib3

class TelegramBot:
    def __init__(self, bot_token, chat_id, message):
        # Inisialisasi atribut-atribut bot
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.message = message
        self.interval = 5
        self.num_requests = 10
        self.url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"

    def send_message(self, text):
        # Fungsi untuk mengirim pesan ke Telegram
        http = urllib3.PoolManager()
        headers = {'Content-Type': 'application/json'}
        data = {"chat_id": self.chat_id, "text": text}
        
        try:
            # Melakukan request POST ke API Telegram
            http.request('POST', self.url, body=json.dumps(data).encode('utf-8'), headers=headers)
            print(f"Pesan '{text}' berhasil dikirim!!.")
        except urllib3.exceptions.HTTPError as e:
            # Menangani kesalahan HTTP
            print(f"HTTP Error: {e}")
            if e.status == 429:
                # Jika terjadi HTTP 429 (Terlalu Banyak Permintaan), tunggu sesuai Retry-After header
                retry_after = e.headers.get('Retry-After')
                print(f"Too many requests, retrying after {retry_after} seconds.")
                time.sleep(int(retry_after))
                self.send_message(text)  # Coba kirim pesan lagi
        except urllib3.exceptions.URLError as e:
            # Menangani kesalahan URL
            print(f"URL Error: {e}")
        except Exception as e:
            # Menangani kesalahan umum
            print(f"An unexpected error occurred: {e}")

    def send_messages_continuously(self):
        # Fungsi untuk mengirim pesan secara berulang-ulang
        count = 0
        try:
            while count < self.num_requests:
                self.send_message(self.message)
                time.sleep(self.interval)
                count += 1
        except KeyboardInterrupt:
            # Tangani jika pengguna mematikan bot secara manual
            print("Bot stopped manually.")

if __name__ == "__main__":
# Example url Detail to get botToken, chatId
# https://api.telegram.org/bot6680557007:AAGmHtzlEVGXJxKxxF62tUPFx9kmYeqk5QQ/sendMessage?parse_mode=markdown&chat_id=6465082908&text=hallo
    bot = TelegramBot(
        bot_token="6680557007:AAGmHtzlEVGXJxKxxF62tUPFx9kmYeqk5QQ",
        chat_id="6465082908",
        message="Hello bro"
    )
    bot.send_messages_continuously()
