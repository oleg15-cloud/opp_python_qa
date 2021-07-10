from src.figure import Figure
from math import pi


class Circle(Figure):

    def __init__(self, radius):
        self.radius = radius
        self.name = "Circle"

    @property
    def perimeter(self):
        return round(2 * pi * self.radius, 2)

    @property
    def area(self):
        return round(pi * self.radius ** 2, 2)
