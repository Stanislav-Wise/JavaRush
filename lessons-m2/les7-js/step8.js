// function sum(a, b) {
//     let c = 100;
//     return a + b + c;
//
// }
//
// let result = sum(10, 20);
// console.log(result);
// console.log(c);


let c = 100;

function sum(a, b) {
    // let c = 50;
    c += 100
    return a + b + c;
}

let result = sum(10, 20);
console.log(result);
console.log(c);