const person = {
    name: 'John',
    age: 30,
    sayHello() {
        console.log(`Hello, my name is ${this.name} and I'm ${this.age} years old.`);
    }
};

person.sayHello();

console.log(Object.getPrototypeOf(person));


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


Object.setPrototypeOf(person, animal);

console.log(Object.getPrototypeOf(person));


const bird = Object.create(dog);

console.log(Object.getPrototypeOf(bird));