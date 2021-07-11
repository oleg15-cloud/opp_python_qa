import pytest


def test_add_square_area_to_triangle(default_triangle, default_square):
    """Check sum area of triangle and square"""
    total_area = default_triangle.add_area(default_square)
    assert total_area == default_triangle.area + default_square.area


def test_add_circle_area_to_triangle(default_triangle, default_circle):
    """Check sum area of triangle and circle"""
    total_area = default_triangle.add_area(default_circle)
    assert total_area == default_triangle.area + default_circle.area


def test_add_rectangle_area_to_triangle(default_triangle, default_rectangle):
    """Check sum area of triangle and rectangle"""
    total_area = default_triangle.add_area(default_rectangle)
    assert total_area == default_triangle.area + default_rectangle.area


def test_add_triangle_area_to_square(default_square, default_triangle):
    """Check sum area of square and triangle"""
    total_area = default_square.add_area(default_triangle)
    assert total_area == default_square.area + default_triangle.area


def test_add_circle_area_to_square(default_square, default_circle):
    """Check sum area of square and circle"""
    total_area = default_square.add_area(default_circle)
    assert total_area == default_square.area + default_circle.area


def test_add_rectangle_area_to_square(default_square, default_rectangle):
    """Check sum area of square and rectangle"""
    total_area = default_square.add_area(default_rectangle)
    assert total_area == default_square.area + default_rectangle.area


def test_add_square_area_to_rectangle(default_rectangle, default_square):
    """Check sum area of rectangle and square"""
    total_area = default_rectangle.add_area(default_square)
    assert total_area == default_rectangle.area + default_square.area


def test_add_triangle_area_to_rectangle(default_rectangle, default_triangle):
    """Check sum area of rectangle and triangle"""
    total_area = default_rectangle.add_area(default_triangle)
    assert total_area == default_rectangle.area + default_triangle.area


def test_add_circle_area_to_rectangle(default_rectangle, default_circle):
    """Check sum area of rectangle and circle"""
    total_area = default_rectangle.add_area(default_circle)
    assert total_area == default_rectangle.area + default_circle.area


def test_add_square_area_to_circle(default_circle, default_square):
    """Check sum area of circle and square"""
    total_area = default_circle.add_area(default_square)
    assert total_area == default_circle.area + default_square.area


def test_add_triangle_area_to_circle(default_circle, default_triangle):
    """Check sum area of circle and triangle"""
    total_area = default_circle.add_area(default_triangle)
    assert total_area == default_circle.area + default_triangle.area


def test_add_rectangle_area_to_circle(default_circle, default_rectangle):
    """Check sum area of circle and rectangle"""
    total_area = default_circle.add_area(default_rectangle)
    assert total_area == default_circle.area + default_rectangle.area


def test_incorrect_class_into_add_area_method(default_triangle):
    """Check incorrect class into add_area() method"""

    class Animal:
        pass

    cat = Animal()
    with pytest.raises(ValueError):
        assert default_triangle.add_area(cat)
