const axios = require("axios");

// Variabel konfigurasi
const config = {
   botToken: "6680557007:AAGmHtzlEVGXJxKxxF62tUPFx9kmYeqk5QQ",
   chatId: "6465082908",
   message: "hallo bro",
   interval: 5000,
   requestRetryInterval: 30000,
};

// Fungsi untuk mengirim pesan menggunakan axios
async function sendMessage(text) {
   const url = `https://api.telegram.org/bot${config.botToken}/sendMessage`;
   try {
      await axios.post(url, {
         chat_id: config.chatId,
         text: text,
      });
      console.log("Berhasil melakukan SPAM");
   } catch (error) {
      handleError(error);
   }
}

// Fungsi utama untuk mengirim pesan secara terus menerus dengan interval
async function sendMessagesContinuously() {
   while (true) {
      await sendMessage(config.message);
      await sleep(config.interval);
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
