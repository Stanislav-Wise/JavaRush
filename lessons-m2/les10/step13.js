class Animal {
    constructor(name) {
        this.name = name;
    }
    eat() {
        console.log(`${this.name} ест`);
    }
}


class Dog extends Animal {
    constructor(name, age) {
        super(name);
        this.age = age;
    }

    sleep() {
        console.log(`${this.name} ${this.age} спит`);
    }
    eat() {
        console.log(`${this.name} жуёт`);
    }
}


const dog = new Dog('Sharik', 12);
dog.eat();
dog.sleep();