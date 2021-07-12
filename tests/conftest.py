import pytest

from math import sqrt, pi
from src.triangle import Triangle
from src.square import Square
from src.circle import Circle
from src.rectangle import Rectangle


@pytest.fixture()
def default_triangle():
    triangle = Triangle(a=13, b=14, c=15)
    yield triangle
    del triangle


@pytest.fixture()
def perimeter_of_triangle(default_triangle):
    return round(default_triangle.a + default_triangle.b + default_triangle.c, 2)


@pytest.fixture()
def area_of_triangle(default_triangle):
    part_of_perimeter = (default_triangle.a + default_triangle.b + default_triangle.c) / 2
    return round(
        sqrt(part_of_perimeter * (part_of_perimeter - default_triangle.a) * (part_of_perimeter - default_triangle.b) * (
                part_of_perimeter - default_triangle.c)), 2)


@pytest.fixture()
def default_square():
    square = Square(10)
    yield square
    del square


@pytest.fixture()
def perimeter_of_square(default_square):
    return round(default_square.a * 4, 2)


@pytest.fixture()
def area_of_square(default_square):
    return round(default_square.a ** 2, 2)


@pytest.fixture()
def default_circle():
    circle = Circle(7)
    yield circle
    del circle


@pytest.fixture()
def perimeter_of_circle(default_circle):
    return round(2 * pi * default_circle.radius, 2)


@pytest.fixture()
def area_of_circle(default_circle):
    return round(pi * default_circle.radius ** 2, 2)


@pytest.fixture()
def default_rectangle():
    rectangle = Rectangle(10, 15)
    yield rectangle
    del rectangle


@pytest.fixture()
def perimeter_of_rectangle(default_rectangle):
    return round(2 * (default_rectangle.length + default_rectangle.height), 2)


@pytest.fixture()
def area_of_rectangle(default_rectangle):
    return round(default_rectangle.length * default_rectangle.height, 2)
