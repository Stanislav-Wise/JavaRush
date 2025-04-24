const socket = new WebSocket("wss://echo.websocket.org");


socket.addEventListener("open", () => {
  console.log("✅ Соединение установлено");
});


socket.addEventListener("message", (event) => {
  console.log("📨 Получено сообщение:", event.data);
});


socket.addEventListener("error", (event) => {
  console.error("❌ Произошла ошибка WebSocket", event);
});


socket.addEventListener("close", (event) => {
  console.log("🔒 Соединение закрыто");
  console.log("Код:", event.code);
  console.log("Причина:", event.reason);
});


document.getElementById("sendBtn").addEventListener("click", () => {
  if (socket.readyState === WebSocket.OPEN) {
    const message = "Привет, сервер!";
    socket.send(message);
    console.log("📤 Отправлено:", message);
  } else {
    console.log("⚠️ Соединение не открыто");
  }
});


document.getElementById("closeBtn").addEventListener("click", () => {
  if (socket.readyState === WebSocket.OPEN) {
    socket.close(1000, "Пользователь закрыл соединение");
  } else {
    console.log("⚠️ Соединение уже закрыто");
  }
});
