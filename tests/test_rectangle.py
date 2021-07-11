def test_name_of_rectangle(default_rectangle):
    """Check name of rectangle"""
    assert default_rectangle.name == "Rectangle"


def test_perimeter_of_rectangle(default_rectangle, perimeter_of_rectangle):
    """Check perimeter of Rectangle"""
    assert default_rectangle.perimeter == perimeter_of_rectangle


def test_area_of_rectangle(default_rectangle, area_of_rectangle):
    """Check area of Rectangle"""
    assert default_rectangle.area == area_of_rectangle
