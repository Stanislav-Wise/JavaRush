let name = 'Ann'
let job = 'work'

let student = {
    name: job,
};

console.log(student);


let student1 = {
    [name]: job,
};

console.log(student1);
console.log(student1[name]);

student1[name] = 'Bob';
console.log(student1);

student1['123'] = 'Bob';
console.log(student1);


let student2 = {
    ['friend' + name]: job + '123',
};

console.log(student2);
