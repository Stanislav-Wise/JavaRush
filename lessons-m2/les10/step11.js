class BankAccount {
    #balance = 0;

    deposit(amount) {
        if (amount > 0) {
            this.#balance += amount;
        }
    }

    #logBalance() {
        console.log(`Balance: ${this.#balance}`);
    }

    show() {
        this.#logBalance();
    }
}

const obj = new BankAccount();
obj.show();
obj.deposit(100);
obj.show();

