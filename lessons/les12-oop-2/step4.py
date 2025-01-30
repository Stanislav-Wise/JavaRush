class Vehicle:
    def __init__(self, color, max_speed):
        print('Инициализация класса Vehicle')
        self.color = color
        self.max_speed = max_speed

    def move(self):
        print(f"{self.color} vehicle is moving at {self.max_speed} km/h")


class Car(Vehicle):
    def __init__(self, color, max_speed, engine_type):
        print('Инициализация класса Car')
        super().__init__(color, max_speed)
        self.engine_type = engine_type

    def move(self):
        print(f"{self.color} vehicle is moving at {self.max_speed} km/h  type engine {self.engine_type}")


class ElectricCar(Car):
    def __init__(self, color, max_speed):
        print('Инициализация класса ElectricCar')
        super().__init__(color, max_speed, 'electric')
        self.battery = 100

    def move(self):
        super().move()
        print('Работает тихо и бесшумно')

    def sound(self):
        print('Beep-beep')


car_1 = Car('red', 120, 'gas')

car_2 = Car('white', 150, 'diesel')

car_1.move()
car_2.move()


tesla = ElectricCar('black', 200)

tesla.move()
print(tesla.battery)

tesla.sound()


print(issubclass(ElectricCar, Car))
print(issubclass(ElectricCar, Vehicle))
print(issubclass(Car, Vehicle))
print(issubclass(Car, ElectricCar))

