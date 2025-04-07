let name = 'Ann';
let age = 30;


let user = {
    name: name,
    age: age,
    friend: null,
};


for (let key in user) {
    console.log(`${key}: ${user[key]}`);
}