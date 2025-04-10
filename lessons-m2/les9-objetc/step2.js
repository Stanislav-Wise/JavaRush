function divide(a, b) {
  if (b === 0) {
    throw new Error("Деление на ноль запрещено!");
  }
  return a / b;
}

try {
  const result = divide(10, 0);
  console.log(result);
} catch (error) {
  console.error("Ошибка:", error.message);
}