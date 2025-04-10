// function fibonacci(n) {
//     if (n <= 1) {
//         return n;
//     }
//     return fibonacci(n - 1) + fibonacci(n - 2);
// }
//
// const result = fibonacci(30);
// console.log(result);


function fibonacci(n, memo = {}) {
    if (n in memo) {
        return memo[n];
    }

    if (n <= 1) {
        return n;
    }

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo);
    return memo[n];
}

const result1 = fibonacci(40);
console.log(result1);

const result2 = fibonacci(30);
console.log(result2);

const result3 = fibonacci(40);
console.log(result3);

const result4 = fibonacci(50);
console.log(result4);