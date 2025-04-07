function User(name, age) {
    this.name = name;
    this.age = age;

    this.greet = function () {
        console.log(`Hello, ${this.name}, ${this.age} лет!`)
    }
}


const user = new User('Ann', 30);
console.log(user)
user.greet();
const user1 = new User('Bob', 25);
console.log(user1)
user1.greet();