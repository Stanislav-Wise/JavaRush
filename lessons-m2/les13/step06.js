let socket;

function connectWebSocket() {
  socket = new WebSocket("wss://echo.websocket.org");
  const statusEl = document.getElementById("status");

  socket.onopen = () => {
    console.log("✅ Соединение установлено");
    statusEl.textContent = "Статус: ✅ соединение открыто";
  };

  socket.onmessage = (event) => {
    console.log("📨 Получено сообщение:", event.data);
  };

  socket.onerror = (event) => {
    console.error("❌ Ошибка WebSocket:", event);
    statusEl.textContent = "Статус: ❌ произошла ошибка соединения";
    alert("Ошибка соединения. Попробуем переподключиться...");
  };

  socket.onclose = (event) => {
    console.warn("⚠️ Соединение закрыто:", event.code, event.reason);
    statusEl.textContent = `Статус: 🔁 закрыто (${event.code})`;

    if (event.code !== 1000) {
      console.log("Попытка переподключения через 3 секунды...");
      setTimeout(connectWebSocket, 3000);
    }
  };
}


connectWebSocket();
