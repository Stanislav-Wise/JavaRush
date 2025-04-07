const user1 = {
    name: 'Bob',
    age: 23,
    greet: function(greeting) {
        console.log(`${greeting}, ${this.name}, ${this.age} лет!`)
    }
};


const user2 = {
    name: 'Ann',
    age: 17,
};

console.log(user1)
console.log(user2)
user1.greet('Привет')

user1.greet.call(user2, 'Пока')
user1.greet.apply(user2, ['Пока'])


