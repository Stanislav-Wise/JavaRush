function divide(a, b) {
  if (b === 0) {
    throw new Error("На ноль делить нельзя!");
  }
  return a / b;
}

try {
  try {
    let result = divide(10, 0); // ошибка тут
    console.log("Результат:", result);
  } catch (innerError) {
    console.warn("Внутренняя ошибка:", innerError.message);
    throw innerError; // пробрасываем дальше
  }
} catch (outerError) {
  console.error("Внешняя ошибка:", outerError.message);
} finally {
  console.log("Завершение вычислений.");
}