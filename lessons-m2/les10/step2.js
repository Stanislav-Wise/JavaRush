const human = {
    breathe() {
        console.log('Дыхание');
    }
}


const developer = Object.create(human);
developer.code = function () {
    console.log('Код');
}


const frontendDev = Object.create(developer);

frontendDev.breathe();
frontendDev.code();


