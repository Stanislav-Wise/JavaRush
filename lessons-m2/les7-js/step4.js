// // Пример пользовательского преобразования
// const user = {
// name: "Alice",
// age: 30,
// valueOf() {
// return this.age;
// },
// toString() {
// return this.name;
// }
// };
// console.log(user + 10);
//  // 40 (valueOf)
// console.log(user + "!")
//  // "Alice!" (toString)
// console.log(String(user));
//  // "Alice"
// console.log(Number(user));
//  // 30

//
// // Примеры преобразования в число
// console.log(Number(true));
//  // 1
// console.log(Number(false));
//  // 0
// console.log(Number(null));
//  // 0
// console.log(Number(undefined)); // NaN
// console.log(Number("123"));
// console.log(Number("12345abc"));
// console.log(Number("1234.567"));
//  // 123
// console.log(Number("abc"));
//  // NaN
// console.log(Number([]));
//  // 0
// console.log(Number({}));
//  // NaN



console.log(String(true));
 // "true"
console.log(String(false));
 // "false"
console.log(String(null));
 // "null"
console.log(String(undefined)); // "undefined«
console.log(String(42));
 // "42"
console.log(String([]));
 // ""
console.log(String([1,2,3]));
 // "1,2,3"
console.log(String({}));
 // "[object Object]"