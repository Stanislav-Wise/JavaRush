const myDate = 'December 28, 2023 10:00:00';
console.log(myDate);
console.log(typeof myDate);

const ms = Date.parse(myDate);

console.log(ms);
console.log(new Date(ms));