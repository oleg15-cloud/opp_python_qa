class Figure:
    name = None
    area = None
    perimeter = None

    def __init__(self, name, area, perimeter):
        self.name = name
        self.area = area
        self.perimeter = perimeter

    def add_area(self, obj):
        if isinstance(obj, Figure):
            return round(self.area + obj.area, 2)
        else:
            raise ValueError(f"Incorrect class of object. This object is not a geometric figure")
