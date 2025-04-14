class Animal {
    constructor(name) {
        this.name = name;
    }
    eat() {
        console.log(`${this.name} ест`);
    }
}


const cat = new Animal('Murzik');
cat.eat();