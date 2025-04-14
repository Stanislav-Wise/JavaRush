class Animal {
    constructor(name) {
        this.name = name;
    }
    eat() {
        console.log(`${this.name} ест`);
    }
}


//
// function Animal(name) {
//     this.name = name;
// }
//
// Animal.prototype.eat = function () {
//     console.log(`${this.name} ест`);
// }

const cat = new Animal('Murzik');
cat.eat();
console.log(cat.__proto__ === Animal.prototype);