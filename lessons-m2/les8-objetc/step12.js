let user = {
    friend: null,
    name: 'Ann',
    age: 22,
    '2': 'one',
    '4': 'two',
    '1': 'three',
    '34': 'four',
};

console.log(user)
console.log('age' in user)
console.log(user.hasOwnProperty('name'))
console.log(user.hasOwnProperty('name12'))

if ('name' in user) {
    console.log(user.name);
}
console.log(user.city)
