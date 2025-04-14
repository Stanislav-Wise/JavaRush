class MyClass {
    #hidden = 42;

    #logHidden() {
        console.log(this.#hidden);
    }

    show() {
        this.#logHidden();
    }
}

const obj = new MyClass();
obj.#logHidden();

