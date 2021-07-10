from src.figure import Figure


class Square(Figure):

    def __init__(self, a):
        super().__init__(self.name, self.area, self.perimeter)
        self.a = a
        self.name = "Square"
        self.area = self.get_area_of_square()
        self.perimeter = self.get_perimeter_of_square()

    def get_perimeter_of_square(self):
        return round(self.a * 4, 2)

    def get_area_of_square(self):
        return round(self.a ** 2, 2)
