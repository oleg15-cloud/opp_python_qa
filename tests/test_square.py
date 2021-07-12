def test_name_of_square(default_square):
    """Check name of square"""
    assert default_square.name == "Square"


def test_perimeter_of_square(default_square, perimeter_of_square):
    """Check perimeter of square"""
    assert default_square.perimeter == perimeter_of_square


def test_area_of_square(default_square, area_of_square):
    """Check area of square"""
    assert default_square.area == area_of_square
