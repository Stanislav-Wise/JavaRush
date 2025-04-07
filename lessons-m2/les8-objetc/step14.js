const user1 = {
    name: 'Ann',
    age: 17,
};

// let user2 = user1;
//
// console.log(user1)
// user2.name = 'Bob';
console.log(user1)


let user3 = Object.assign({}, user1);

user3.name = 'Bob';
let user4 = {};

for (let key in user1) {
    user4[key] = user1[key];
}

user4.name = 'Bob4';

console.log(user1)
console.log(user3)
console.log(user4)




