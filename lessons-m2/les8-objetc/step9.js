let name = 'Ann';
let age = 30;


let user = {
    friend: null,
    name: name,
    age: age,
    '2': 'one',
    '4': 'two',
    '1': 'three',
    '34': 'four',

};


for (let key in user) {
    console.log(`${key}: ${user[key]}`);
}

console.log(user)