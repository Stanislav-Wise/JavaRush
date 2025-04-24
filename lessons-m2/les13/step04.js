// 7

const socket = new WebSocket("wss://echo.websocket.org", ["soap", "wamp"]);

socket.onopen = () => {
  console.log("Соединение открыто");
  console.log("Выбранный подпротокол:", socket.protocol);
};