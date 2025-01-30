class Car:
    def drive(self, city):
        print(f"Driving to {city}")


class RoboDelivery:
    def drive(self, city):
        print(f"Robo go to {city}")

    def delivery(self, address):
        print(f'Доставляем по адресу {address}')


class RoboCar(Car, RoboDelivery):
    pass


rc = RoboCar()
rc.drive('Москва')
rc.delivery("Красная площадь, 1")
