self.onmessage = function (event) {
  if (event.data === "start") {
    let sum = 0;
    for (let i = 1; i <= 1_000_000_000; i++) {
      sum += i;
    }
    self.postMessage(sum);
  }
};