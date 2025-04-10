function greet(name) {
    console.log(`Hello, ${name} !`);

}

setInterval(greet, 2000, 'John');

console.log('end');

clearInterval()