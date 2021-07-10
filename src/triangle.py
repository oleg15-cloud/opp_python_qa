from src.figure import Figure
from math import sqrt


class Triangle(Figure):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.name = "Triangle"

    def is_it_triangle(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return True
        else:
            return None

    @property
    def perimeter(self):
        if self.is_it_triangle() is True:
            return round(self.a + self.b + self.c, 2)
        else:
            return None

    @property
    def area(self):
        if self.is_it_triangle() is True:
            part_of_perimeter = (self.a + self.b + self.c) / 2
            return round(sqrt(part_of_perimeter * (part_of_perimeter - self.a) * (part_of_perimeter - self.b) * (
                    part_of_perimeter - self.c)), 2)
        else:
            return None
