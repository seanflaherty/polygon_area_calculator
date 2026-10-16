"""Tests for polygon_area_calculator."""
# scf import pytest
from src.polygon_area_calculator import Rectangle, Square

def test_rectangle_initialization_and_str():
    """Test rectangle creation and string representation."""
    rect = Rectangle(4, 5)
    assert rect.width == 4
    assert rect.height == 5
    assert str(rect) == "Rectangle(width=4, height=5)"

def test_rectangle_setters():
    """Test width and height setters for Rectangle."""
    rect = Rectangle(2, 3)
    rect.set_width(10)
    rect.set_height(20)
    assert rect.width == 10
    assert rect.height == 20

def test_rectangle_calculations():
    """Test area, perimeter, and diagonal calculations."""
    rect = Rectangle(3, 4)
    assert rect.get_area() == 12
    assert rect.get_perimeter() == 14
    # 3-4-5 right triangle diagonal
    assert rect.get_diagonal() == 5.0

def test_rectangle_picture_normal():
    """Test picture string generation for valid sizes."""
    rect = Rectangle(2, 3)
    expected = "**\n**\n**\n"
    assert rect.get_picture() == expected


def test_rectangle_picture_too_big():
    """Test picture string limit when dimensions exceed 50."""
    rect1 = Rectangle(51, 10)
    rect2 = Rectangle(10, 51)

    assert rect1.get_picture() == "Too big for picture."
    assert rect2.get_picture() == "Too big for picture."


def test_rectangle_get_amount_inside():
    """Test how many times one shape fits inside another."""
    outer = Rectangle(10, 10)
    inner = Rectangle(3, 3)

    # 10 // 3 = 3 horizontally; 10 // 3 = 3 vertically -> 3 * 3 = 9
    assert outer.get_amount_inside(inner) == 9

    # Test when inner shape is larger than outer
    tiny = Rectangle(20, 20)
    assert outer.get_amount_inside(tiny) == 0


def test_square_initialization_and_str():
    """Test square creation, inheritance, and string representation."""
    sq = Square(5)
    assert sq.width == 5
    assert sq.height == 5
    assert str(sq) == "Square(side=5)"


def test_square_setters():
    """Test that modifying side, width, or height keeps the square symmetric."""
    sq = Square(4)

    sq.set_side(6)
    assert sq.width == 6
    assert sq.height == 6
    assert str(sq) == "Square(side=6)"

    sq.set_width(8)
    assert sq.width == 8
    assert sq.height == 8

    sq.set_height(10)
    assert sq.width == 10
    assert sq.height == 10


def test_square_inherited_methods():
    """Test that Square correctly inherits and uses Rectangle methods."""
    sq = Square(3)
    assert sq.get_area() == 9
    assert sq.get_perimeter() == 12
    assert sq.get_diagonal() == (3**2 + 3**2) ** 0.5

    # Square inside a rectangle
    rect = Rectangle(10, 10)
    assert rect.get_amount_inside(sq) == 9  # 10 // 3 = 3 -> 3 * 3 = 9
