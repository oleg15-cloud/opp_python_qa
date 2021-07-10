from src.figure import Figure


class Rectangle(Figure):

    def __init__(self, length, height):
        super().__init__(self.name, self.area, self.perimeter)
        self.length = length
        self.height = height
        self.name = "Rectangle"
        self.area = self.get_area_of_rectangle()
        self.perimeter = self.get_perimeter_of_rectangle()

    def get_perimeter_of_rectangle(self):
        return round(2 * (self.length + self.height), 2)

    def get_area_of_rectangle(self):
        return round(self.length * self.height, 2)
