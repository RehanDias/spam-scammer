import json
import urllib.request
import time

class TelegramBot:
    def __init__(self, bot_token, chat_id, message):
        # Inisialisasi variabel-variabel yang diperlukan
        self.bot_token = bot_token  # Token bot Telegram
        self.chat_id = chat_id  # ID obrolan untuk mengirim pesan
        self.message = message  # Pesan yang akan dikirim
        self.interval = 5  # Interval waktu dalam detik antara setiap pengiriman pesan
        self.retry_interval = 30  # Interval waktu dalam detik sebelum mencoba lagi setelah mendapatkan kesalahan 429 (Batas permintaan tercapai)
        self.num_requests = 10  # Jumlah total permintaan yang akan dikirim

        # URL untuk mengirim pesan menggunakan Telegram Bot API
        self.url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"

    def send_message(self, text):
        # Membuat data JSON untuk pesan yang akan dikirim
        data = {
            "chat_id": self.chat_id,
            "text": text
        }
        try:
            # Membuka URL dengan pengaturan khusus
            opener = urllib.request.build_opener(urllib.request.HTTPSHandler())
            req = urllib.request.Request(self.url, json.dumps(data).encode("utf-8"), headers={'Content-Type': 'application/json'})
            with opener.open(req) as response:
                response_data = json.loads(response.read().decode("utf-8"))
                # Memeriksa apakah pesan berhasil dikirim
                if response_data["ok"]:
                    print(f"Pesan '{text}' berhasil dikirim, Berhasil melakukan SPAM")
                else:
                    print("Failed to send message:", response_data["description"])
        except urllib.error.HTTPError as e:
            self.handle_http_error(e)
        except urllib.error.URLError as e:
            self.handle_url_error(e)
        except Exception as e:
            print("An error occurred:", e)

    def handle_http_error(self, error):
        print("HTTP Error:", error)
        if error.code == 429:  # Too Many Requests error
            try:
                response_data = json.loads(error.read().decode("utf-8"))
                retry_after = response_data["parameters"]["retry_after"]
                print(f"Too Many Requests: Retry after {retry_after} seconds")
                time.sleep(int(retry_after))
                self.send_messages_continuously()  # Panggil kembali fungsi untuk melanjutkan pengiriman pesan
            except Exception as e:
                print("Failed to handle Too Many Requests error:", e)
                time.sleep(self.retry_interval)
                self.send_messages_continuously()

    def handle_url_error(self, error):
        print("URL Error:", error)

    def send_messages_continuously(self):
        count = 0
        while count < self.num_requests:
            try:
                self.send_message(self.message)
                time.sleep(self.interval)
                count += 1
            except Exception as e:
                print("An error occurred:", e)
                time.sleep(self.retry_interval)

# Inisialisasi dan penggunaan objek TelegramBot
# Example url Detail to get botToken, chatId
# https://api.telegram.org/bot6680557007:AAGmHtzlEVGXJxKxxF62tUPFx9kmYeqk5QQ/sendMessage?parse_mode=markdown&chat_id=6465082908&text=hallo
bot = TelegramBot(
    bot_token="6680557007:AAGmHtzlEVGXJxKxxF62tUPFx9kmYeqk5QQ", # Token bot Telegram
    chat_id="6465082908", # ID chat untuk mengirim pesan
    message="Hello bro" # Pesan yang akan dikirim
)
bot.send_messages_continuously()
