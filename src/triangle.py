from src.figure import Figure
from math import sqrt


class Triangle(Figure):
    name = "Triangle"
    area = None
    perimeter = None

    def __init__(self, a, b, c):
        super().__init__(self.name, self.area, self.perimeter)
        self.a = a
        self.b = b
        self.c = c
        self.area = self.get_area_of_triangle()
        self.perimeter = self.get_perimeter_of_triangle()

    def is_it_triangle(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return True
        else:
            return None

    def get_perimeter_of_triangle(self):
        if self.is_it_triangle() is True:
            return round(self.a + self.b + self.c, 2)
        else:
            return None

    def get_area_of_triangle(self):
        if self.is_it_triangle() is True:
            part_of_perimeter = (self.a + self.b + self.c) / 2
            return round(sqrt(part_of_perimeter * (part_of_perimeter - self.a) * (part_of_perimeter - self.b) * (
                    part_of_perimeter - self.c)), 2)
        else:
            return None
