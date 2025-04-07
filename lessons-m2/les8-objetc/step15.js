// Spread (...)

const user1 = {
    name: 'Ann',
    age: 17,
};


let user2 = {...user1};

console.log(user1)
user2.name = 'Bob';

console.log(user1)
console.log(user2)


let a = [1, 2, 3];
let b = [...a];
b.push(4);
console.log(a);
console.log(b);


const userAdd = {
    name: 'Bob',
    age: 17,
    isFriend: true,
};

const user3 = {...user1, ...userAdd};
console.log(user3)

const user5 = {...userAdd, ...user1};
console.log(user5)