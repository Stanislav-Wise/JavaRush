const personPrototype = {
    greet() {
        console.log(`Hello, World!} !`);
    }
}

const student = Object.create(personPrototype);

student.greet();

// console.log(student.__proto__ === personPrototype);
console.log(student.__proto__);