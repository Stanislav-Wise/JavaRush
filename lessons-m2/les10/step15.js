class User {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    sayHello() {
        console.log(`Hello, my name is ${this.name} and I'm ${this.age} years old.`);
    }

    static createUser() {
        return new User("Anonimus", 20);
    }
}

const user = User.createUser();
user.sayHello();