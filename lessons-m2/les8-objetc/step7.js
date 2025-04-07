let name = 'Ann';
let age = 30;


let user = {
    name: name,
    age: age,
    friend: null,
};

let friend1 = 'Bob';
let friend2 = 'name';
console.log(user)
console.log('name' in user)
console.log('age' in user)
console.log('Bob' in user)
console.log(friend1 in user)
console.log(friend2 in user)

