// function outer() {
//     let message = 'Внешняя функция';
//
//     function inner() {
//         // let message = 'Внутренняя функция';
//         console.log(message);
//     }
//
//     return inner;
// }
//
// const sayMessage = outer();
// sayMessage();


function outer() {
    let count = 0;

    return function () {
        count++;
        console.log(count);
    };
}




const sayCount = outer();
sayCount();
sayCount();
sayCount();
console.log(sayCount.count)