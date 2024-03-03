import json
import urllib.request
import time

class TelegramBot:
    def __init__(self, bot_token, chat_id, message):
        # Inisialisasi atribut-atribut bot
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.message = message
        self.interval = 5  # Interval waktu antara pengiriman pesan
        self.retry_interval = 30  # Interval waktu untuk mencoba kembali setelah kesalahan
        self.num_requests = 10  # Jumlah pesan yang akan dikirim
        # URL untuk mengirim pesan menggunakan API Telegram
        self.url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"

    def send_message(self, text):
        # Mengirim pesan ke Telegram
        data = {
            "chat_id": self.chat_id,
            "text": text
        }
        try:
            opener = urllib.request.build_opener(urllib.request.HTTPSHandler())
            req = urllib.request.Request(self.url, json.dumps(data).encode("utf-8"), headers={'Content-Type': 'application/json'})
            with opener.open(req) as response:
                response_data = response.read().decode("utf-8")
                if "ok" in response_data:
                    print(f"Pesan '{text}' berhasil dikirim.")
                else:
                    print("Gagal mengirim pesan:", response_data)
        except urllib.error.HTTPError as e:
            self.handle_http_error(e)
        except urllib.error.URLError as e:
            self.handle_url_error(e)
        except Exception as e:
            print("Terjadi kesalahan:", e)

    def handle_http_error(self, error):
        # Menangani kesalahan HTTP
        print("HTTP Error:", error)
        if error.code == 429:  # Kode status 429: Terlalu Banyak Permintaan
            try:
                response_data = json.loads(error.read().decode("utf-8"))
                retry_after = response_data["parameters"]["retry_after"]
                print(f"Terlalu banyak permintaan: coba lagi setelah {retry_after} detik")
                time.sleep(int(retry_after))
            except Exception as e:
                print("Gagal menangani kesalahan Terlalu Banyak Permintaan:", e)
            finally:
                self.send_messages_continuously()

    def handle_url_error(self, error):
        # Menangani kesalahan URL
        print("URL Error:", error)

    def send_messages_continuously(self):
        # Mengirim pesan secara berulang-ulang
        count = 0
        while count < self.num_requests:
            try:
                self.send_message(self.message)
                time.sleep(self.interval)
                count += 1
            except Exception as e:
                print("Terjadi kesalahan:", e)
                time.sleep(self.retry_interval)

# Penggunaan objek 
# Example url Detail to get botToken, chatId
# https://api.telegram.org/bot6680557007:AAGmHtzlEVGXJxKxxF62tUPFx9kmYeqk5QQ/sendMessage?parse_mode=markdown&chat_id=6465082908&text=hallo
bot = TelegramBot(
    bot_token="6680557007:AAGmHtzlEVGXJxKxxF62tUPFx9kmYeqk5QQ",
    chat_id="6465082908",
    message="Hello bro"
)
bot.send_messages_continuously()
