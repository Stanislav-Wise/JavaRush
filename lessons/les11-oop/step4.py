class Car:
    def __init__(self, color1='white'):
        self.engine_on = False
        self.color = color1

    def start_engine(self):
        self.engine_on = True

    def drive_to(self, city):
        if self.engine_on:
            print(f"Driving to {city}")
        else:
            print("Engine is off")


car_1 = Car('red')
car_1.start_engine()
car_1.drive_to("New York")
print(car_1.color)

print('CAR 2')
car_2 = Car()
car_2.drive_to("Moscow")
print(car_2.color)