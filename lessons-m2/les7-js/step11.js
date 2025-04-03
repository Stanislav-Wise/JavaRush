// function greetUser(name, func) {
//     console.log(func(name));
// }
//
// function formatter(text) {
//     return `Привет, ${text} !!!!`;
// }
//
//
// greetUser('Bob', formatter)


function add_func(num) {
   return function (number) {
       return num + number;
   };
}


let sum = add_func(10);
console.log(typeof sum);
let result = sum(20);
console.log(result);