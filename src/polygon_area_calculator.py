"""Class inheritance example"""
class Rectangle:
    """Rectangle class."""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width: int) -> None:
        """Sets the width of the rectangle based on the supplied integer."""
        self.width = width

    def set_height(self, height: int) -> None:
        """Sets the height of the rectangle based on the supplied integer."""
        self.height = height

    def get_area(self) ->int:
        """Returns the area of the rectangle."""
        return self.width * self.height

    def get_perimeter(self) -> int:
        """Returns the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

    def get_diagonal(self) -> float:
        """Returns the diagonal of the rectangle."""
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self) -> str:
        """Returns a representation of the rectangle using asterix."""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return (("*" * self.width) + "\n") * self.height

    def get_amount_inside(self, shape: "Rectangle") -> int:
        """Returns the area of the rectangle as an integer."""
        return (self.width // shape.width) * (self.height // shape.height)

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    """Square class."""
    def __init__(self, side: int) -> None:
        super().__init__(side, side)

    def set_side(self, side: int) -> None:
        """Sets the side of the square based on the supplied integer."""
        self.width = side
        self.height = side

    def set_width(self, width: int) -> None:
        """Sets the width of the square based on the supplied integer."""
        self.set_side(width)

    def set_height(self, height: int) -> None:
        """Sets the height of the square based on the supplied integer."""
        self.set_side(height)

    def __str__(self) -> str:
        return f"Square(side={self.width})"
