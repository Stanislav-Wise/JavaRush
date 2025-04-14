class Animal {
    constructor(name) {
        this.name = name;
    }

    eat() {
        console.log(`${this.name} ест`);
    }
}

const dog = new Animal('dog');
dog.eat();