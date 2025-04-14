const animal = {
    walk() {
        console.log(`Идёт...`);
    }
}


const dog = {
    eat() {
        console.log('Ест...');
    }
}

dog.__proto__ = animal;

dog.walk();
dog.eat();



