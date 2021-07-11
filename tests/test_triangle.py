import pytest

from src.triangle import Triangle


def test_name_of_triangle(default_triangle):
    """Check name of triangle"""
    assert default_triangle.name == "Triangle"


def test_create_incorrect_triangle():
    """Check creating triangle with incorrect attributes"""
    with pytest.raises(AttributeError):
        Triangle(a=100, b=0, c=0)


def test_perimeter_of_triangle(default_triangle, perimeter_of_triangle):
    """Check parameter of triangle"""
    assert default_triangle.perimeter == perimeter_of_triangle


def test_area_of_triangle(default_triangle, area_of_triangle):
    """Check area of triangle"""
    assert default_triangle.area == area_of_triangle
