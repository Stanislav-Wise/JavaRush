class Animal {
    constructor(name) {
        this.name = name;
    }
    eat() {
        console.log(`${this.name} ест`);
    }
}


class Dog extends Animal {
    sleep() {
        console.log(`${this.name} спит`);
    }
}


const dog = new Dog('Sharik');
dog.eat();
dog.sleep();