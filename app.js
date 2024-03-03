const axios = require("axios");

// Variabel konfigurasi
// Example url Detail to get botToken, chatId
// https://api.telegram.org/bot6680557007:AAGmHtzlEVGXJxKxxF62tUPFx9kmYeqk5QQ/sendMessage?parse_mode=markdown&chat_id=6465082908&text=hallo
const config = {
   botToken: "6680557007:AAGmHtzlEVGXJxKxxF62tUPFx9kmYeqk5QQ",
   chatId: "6465082908",
   message: "hallo",
   interval: 5000,
   requestRetryInterval: 30000,
   numberOfRequests: 10, // Menambahkan numberOfRequests
};

// Fungsi untuk mengirim pesan menggunakan axios
async function sendMessage(text) {
   const url = `https://api.telegram.org/bot${config.botToken}/sendMessage`;
   try {
      const response = await axios.post(url, {
         chat_id: config.chatId,
         text: text,
      });
      console.log(`Pesan "${text}" berhasil dikirim, Berhasil melakukan SPAM`);
   } catch (error) {
      handleError(error);
   }
}

// Fungsi utama untuk mengirim pesan secara terus menerus dengan interval
async function sendMessagesContinuously() {
   let count = 0; // Menambahkan variabel count untuk melacak jumlah request yang telah dilakukan
   while (count < config.numberOfRequests) {
      // Menggunakan numberOfRequests dari konfigurasi
      await sendMessage(config.message);
      await sleep(config.interval);
      count++; // Menambahkan 1 ke count setiap kali request dikirim
   }
}

// Fungsi untuk menangani kesalahan
function handleError(error) {
   console.error("Error:", error.message);
   if (error.response && error.response.status === 429) {
      console.log("Batasan permintaan API telah tercapai. Menunggu...");
      setTimeout(sendMessagesContinuously, config.requestRetryInterval);
   }
}

// Fungsi untuk menunda eksekusi dalam milidetik
function sleep(ms) {
   return new Promise((resolve) => setTimeout(resolve, ms));
}

// Panggil fungsi sendMessagesContinuously untuk memulai pengiriman pesan terus menerus
sendMessagesContinuously().catch((error) => {
   console.error("Terjadi kesalahan fatal:", error.message);
   process.exit(1);
});
