import math


class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Triangle:
    def __init__(self, a, b, c):
        sides = [a, b, c]
        if any(side <= 0 for side in sides):
            raise ValueError("Стороны должны быть положительными")
        if not self._is_valid(sides):
            raise ValueError("Треугольник не существует")
        self.sides = sorted(sides)

    def _is_valid(self, sides):
        a, b, c = sorted(sides)
        return a + b > c

    def area(self):
        a, b, c = self.sides
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

    def is_right(self):
        a, b, c = self.sides
        return abs(a ** 2 + b ** 2 - c ** 2) < 1e-6


def get_area(shape):
    return shape.area()


if __name__ == "__main__":
    circle = Circle(5)
    print(f"Площадь круга: {get_area(circle)}")
    triangle = Triangle(3, 4, 5)
    print(f"Площадь треугольника: {get_area(triangle)}")
    print(f"Прямоугольный: {triangle.is_right()}")
