import json
import urllib.parse
import urllib.request
import time


# Variabel konfigurasi
# Example url Detail to get botToken, chatId
# https://api.telegram.org/bot6680557007:AAGmHtzlEVGXJxKxxF62tUPFx9kmYeqk5QQ/sendMessage?parse_mode=markdown&chat_id=6465082908&text=hallo

config = {
   "botToken": "6680557007:AAGmHtzlEVGXJxKxxF62tUPFx9kmYeqk5QQ",
   "chatId": "6465082908",
   "message": "hallo",
   "interval": 5,
   "requestRetryInterval": 30,
   "numberOfRequests": 10,
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
                print(f"Pesan '{text}' berhasil dikirim: Berhasil melakukan SPAM")
            else:
                print("Gagal mengirim pesan:", response_data["description"])
    except Exception as e:
        handle_error(e)

# Fungsi utama untuk mengirim pesan secara terus menerus dengan interval
def send_messages_continuously():
    count = 0
    while count < config["numberOfRequests"]:
        send_message(config["message"])
        time.sleep(config["interval"])
        count += 1

# Fungsi untuk menangani kesalahan
def handle_error(error):
    print("Error:", error)
    if hasattr(error, "response") and error.response.status_code == 429:
        print("Batasan permintaan API telah tercapai. Menunggu...")
        time.sleep(config["requestRetryInterval"])
        send_messages_continuously()

# Panggil fungsi send_messages_continuously untuk memulai pengiriman pesan terus menerus
send_messages_continuously()
