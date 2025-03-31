// var message = 'Hello';
// console.log(message);
// let count = 0; // Блочная переменная
//
//
// console.log(count);
// const PI = 3.14; // Константа
//
// console.log(PI);
//
//
// let name;


// Примитивные типы
// let num1 = 10;
// let num2 = num1;
// num1 = 20;
// console.log(num1); // 20
// console.log(num2); // 10
// // Ссылочные типы
// let obj1 = { name: 'Alice' };
// let obj2 = obj1;
// obj1.name = 'Bob';
// console.log(obj1.name); // Bob
// console.log(obj2.name); // Bob
//
//
//
// let str1 = 'Одинарными кавычками';
// let str2 = "С двойными кавычками";
// let str3 = `Через обратный апостроф`;


// Многострочная строка
const message = `
This is a multiline
string.
`;

// console.log(message)

// Встраивание выражений
const name = 'John';
const age = 30;
const greeting = `Hello, ${name}! You are
${age} years old.`;

console.log(greeting)

// Форматирование чисел
const price = 123.456;
const formattedPrice = `Price:
$${price.toFixed(2)}`;

Теговый шаблон
function html`<p>${message}</p>`;

console.log(formattedPrice)