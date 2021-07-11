def test_name_of_circle(default_circle):
    """Check name of circle"""
    assert default_circle.name == "Circle"


def test_perimeter_of_circle(default_circle, perimeter_of_circle):
    """Check perimeter of circle"""
    assert default_circle.perimeter == perimeter_of_circle


def test_area_of_circle(default_circle, area_of_circle):
    """Check area of circle"""
    assert default_circle.area == area_of_circle
