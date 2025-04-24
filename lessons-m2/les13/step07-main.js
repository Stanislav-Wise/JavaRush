const startBtn = document.getElementById("startBtn");
const resultEl = document.getElementById("result");

startBtn.onclick = () => {
  const worker = new Worker("step7-worker.js");

  worker.postMessage("start"); // отправляем команду

  worker.onmessage = (event) => {
    resultEl.textContent = `Результат: ${event.data}`;
    worker.terminate(); // останавливаем воркер
  };
};