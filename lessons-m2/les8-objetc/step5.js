let name = 'Ann';
let age = 30;

let user = {
    name,
    age,
};


console.log(user)


let user1 = {
    name: name,
    age: age,
};


console.log(user1)



function makeUser(name, age) {
    return {
        name,
        age,
    };
}

console.log(makeUser('Ann', 30));