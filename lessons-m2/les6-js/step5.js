// let isOnline = false;
// console.log(!isOnline)

//
// const foo = null ?? 'default string';
// console.log(foo);
// // Expected output: "default string"
// const baz = 0 ?? 42;
// console.log(baz);
// // Expected output: 0


console.log(0 == false); // true (неявное преобразование)
console.log(0 === false); // false (разные типы)
console.log("" == false); // true (неявное преобразование)
console.log("" === false); // false (разные типы)
console.log(null == undefined); // true (неявное преобразование)
console.log(null === undefined); // false (разные типы)