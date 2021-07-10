from src.figure import Figure
from math import pi


class Circle(Figure):
    name = "Circle"
    area = None
    perimeter = None

    def __init__(self, radius):
        super().__init__(self.name, self.area, self.perimeter)
        self.radius = radius
        self.area = self.get_area_of_circle()
        self.perimeter = self.get_perimeter_of_circle()

    def get_perimeter_of_circle(self):
        return round(2 * pi * self.radius, 2)

    def get_area_of_circle(self):
        return round(pi * self.radius ** 2, 2)
