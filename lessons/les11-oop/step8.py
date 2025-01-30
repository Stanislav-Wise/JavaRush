from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

    def __str__(self):
        return f'Квадрат со стороной {self.side}. Его площадь {self.area()}, периметр {self.perimeter()}'


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def print_shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


circle = Circle(5)
square = Square(4)
rect = Rectangle(3, 6)

print_shape_info(circle)
print_shape_info(square)
print_shape_info(rect)


# print(dir(circle))
# print(dir(Circle))

# if type(rect) == Circle:
#     print("circle is an instance of Circle")
# else:
#     print("circle is not an instance of Circle")
#
#

circle.name = 'Bob'

if isinstance(circle, Circle):
    print("circle is an instance of Circle")
else:
    print("circle is not an instance of Circle")
#
#
# if isinstance(1.2, int):
#     print("1 is an instance of int")
# else:
#     print("1 is not an instance of int")


print(square)