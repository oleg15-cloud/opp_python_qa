class Figure:

    area = None

    def add_area(self, obj):
        if isinstance(obj, Figure):
            return round(self.area + obj.area, 2)
        else:
            raise ValueError("Incorrect class of object. This object is not a geometric figure")
