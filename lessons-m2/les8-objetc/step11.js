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

for (let key in user) {
    console.log(`${key}: ${user[key]}`);
};

console.log('---');

for (let key of Object.keys(user)) {
    console.log(`${key}`);
};

console.log('---')

for (let value of Object.values(user)) {
    console.log(`${value}`);
};

console.log('---')

for (let [key, value] of Object.entries(user)) {
    console.log(`${key} --- ${value}`);
};