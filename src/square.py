from src.figure import Figure


class Square(Figure):

    def __init__(self, a):
        self.a = a
        self.name = "Square"

    @property
    def perimeter(self):
        return round(self.a * 4, 2)

    @property
    def area(self):
        return round(self.a ** 2, 2)
