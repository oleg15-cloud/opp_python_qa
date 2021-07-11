from src.figure import Figure
from math import sqrt


class Triangle(Figure):

    def __init__(self, a, b, c):
        if a + b > c and a + c > b and b + c > a:
            self.a = a
            self.b = b
            self.c = c
            self.name = "Triangle"
        else:
            raise AttributeError("This triangle is impossible")

    @property
    def perimeter(self):
        return round(self.a + self.b + self.c, 2)


    @property
    def area(self):
        part_of_perimeter = (self.a + self.b + self.c) / 2
        return round(sqrt(part_of_perimeter * (part_of_perimeter - self.a) * (part_of_perimeter - self.b) * (
                part_of_perimeter - self.c)), 2)
