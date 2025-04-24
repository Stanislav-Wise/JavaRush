// 7

const socket = new WebSocket("wss://echo.websocket.org", ["soap", "wamp"]);

socket.onopen = () => {
  console.log("✅ Соединение установлено");
  console.log("Подпротокол выбран сервером:", socket.protocol || "(не выбран)");
};

socket.onmessage = (event) => {
  console.log("📨 Получено:", event.data);
};

socket.onerror = () => {
  console.log("❌ Ошибка соединения");
};

socket.onclose = (event) => {
  console.log("🔒 Соединение закрыто. Код:", event.code);
};