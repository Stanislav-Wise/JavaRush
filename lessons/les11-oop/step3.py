class Greeter:
    def greet(self):
        print(f"Hello, World!")

    def greeting(self, name):
        print(f"Hello, {name}!")


g = Greeter()
g.greet()
g.greeting('Bob')

# Greeter.greet(g)