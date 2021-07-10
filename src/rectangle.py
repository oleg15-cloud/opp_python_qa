from src.figure import Figure


class Rectangle(Figure):

    def __init__(self, length, height):
        self.length = length
        self.height = height
        self.name = "Rectangle"

    @property
    def perimeter(self):
        return round(2 * (self.length + self.height), 2)

    @property
    def area(self):
        return round(self.length * self.height, 2)
