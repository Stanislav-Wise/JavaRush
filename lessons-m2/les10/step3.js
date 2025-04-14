function Person(name) {
    this.name = name;
}


Person.prototype.greet = function () {
    console.log('Привет, меня зовут ' + this.name);
};


const john = new Person('John');
john.greet();

const bob = new Person('Bob');
bob.greet();



