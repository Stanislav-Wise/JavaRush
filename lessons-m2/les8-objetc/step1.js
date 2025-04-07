let user = {
    nameStudent: "John",
    'age 123': 30,
    'name': 'Bob',
    1: 'one',
    оценка: 'пять',
};

let user1 = {};
let user2 = new Object();

console.log(user);
console.log(user['name']);
user['age 123'] = 40;
console.log(user['age 123']);
console.log(user);
console.log(user.nameStudent);
console.log(user.name);
console.log(user.оценка);
console.log(user['1']);

