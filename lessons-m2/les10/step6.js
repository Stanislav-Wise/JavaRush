const animal = {
    walk() {
        console.log(`Идёт...`);
    },
    sleep() {
        console.log(`Спит...`);
    }
}


const dog = Object.create(animal);

dog.eat = function () {
    console.log(`Ест...`);
}


// dog.sleep();
// dog.walk();
// dog.eat();


const cat = Object.create(animal);

cat.walk = function () {
    console.log(`Прыгает...`);
}

cat.sleep();
cat.walk();
// cat.eat();