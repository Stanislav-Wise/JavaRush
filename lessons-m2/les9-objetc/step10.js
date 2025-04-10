function outer() {
    let count = 0;

    return {
        increment() {
            count++;
            console.log(count);
        },
        decrement(){
            count--;
            console.log(count);
        }
    };
}



const sayCount = outer();
sayCount.increment();
sayCount.increment();
sayCount.increment();
sayCount.increment();

sayCount.decrement();

sayCount.increment();

console.log(sayCount.count)

