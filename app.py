import json
import urllib.request
import time

# Variabel konfigurasi
# Example url Detail to get botToken, chatId
# https://api.telegram.org/bot6680557007:AAGmHtzlEVGXJxKxxF62tUPFx9kmYeqk5QQ/sendMessage?parse_mode=markdown&chat_id=6465082908&text=hallo
config = {
    "botToken": "6680557007:AAGmHtzlEVGXJxKxxF62tUPFx9kmYeqk5QQ",  # Token bot Telegram
    "chatId": "6465082908",  # ID obrolan untuk mengirim pesan
    "message": "hallo",  # Pesan yang akan dikirim
    "interval": 5,  # Interval waktu dalam detik antara setiap pengiriman pesan
    "requestRetryInterval": 30,  # Interval waktu dalam detik sebelum mencoba lagi setelah mendapatkan kesalahan 429 (Batas permintaan tercapai)
    "numberOfRequests": 10,  # Jumlah total permintaan yang akan dikirim
}

# Fungsi untuk mengirim pesan menggunakan urllib
def send_message(text):
    url = f"https://api.telegram.org/bot{config['botToken']}/sendMessage"
    data = {
        "chat_id": config["chatId"],
        "text": text
    }
    try:
        req = urllib.request.Request(url, json.dumps(data).encode("utf-8"), headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(req) as response:
            response_data = json.loads(response.read().decode("utf-8"))
            if response_data["ok"]:
                print(f"Pesan '{text}' berhasil dikirim")
            else:
                print("Gagal mengirim pesan:", response_data["description"])
    except urllib.error.HTTPError as e:
        handle_http_error(e)
    except urllib.error.URLError as e:
        handle_url_error(e)

# Fungsi utama untuk mengirim pesan secara terus menerus dengan interval
def send_messages_continuously():
    count = 0
    while count < config["numberOfRequests"]:
        try:
            send_message(config["message"])
            time.sleep(config["interval"])
            count += 1
        except Exception as e:
            print("Terjadi kesalahan:", e)
            time.sleep(config["requestRetryInterval"])

# Fungsi untuk menangani kesalahan HTTP
def handle_http_error(error):
    print("Error HTTP:", error)
    if error.code == 429:
        print("Batasan permintaan API telah tercapai. Menunggu...")
        time.sleep(config["requestRetryInterval"])
        send_messages_continuously()

# Fungsi untuk menangani kesalahan URL
def handle_url_error(error):
    print("Error URL:", error)

# Panggil fungsi send_messages_continuously untuk memulai pengiriman pesan terus menerus
send_messages_continuously()
