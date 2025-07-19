const BOT_TOKEN = "7504653152:AAEtS7QPgdSe5VnUpiCU_GEJXq84i5qKJ4k";  // ← Aapka bot token yahan paste karo
const API_URL = `https://api.telegram.org/bot${BOT_TOKEN}`;

Deno.serve(async (req) => {
  const update = await req.json();
  const message = update.message;
  if (!message) return new Response("no message");

  const chat_id = message.chat.id;
  const text = message.text || "";

  const reply = text === "/start"
    ? "👋 Hello from Deno Deploy!"
    : `You said: ${text}`;

  await fetch(`${API_URL}/sendMessage`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ chat_id, text: reply }),
  });

  return new Response("ok");
});
