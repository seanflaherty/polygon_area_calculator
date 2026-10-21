# Polygon Area Calculator (`polygon_area_calculator`)

> An object-oriented Python application that calculates areas, perimeters, diagonals, and shape shapes using `Rectangle` and `Square` classes. Part of the [freeCodeCamp](https://www.freecodecamp.org/) Python Certification curriculum.

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📌 Overview

This project uses Object-Oriented Programming (OOP) concepts in Python to model geometric polygons. It defines a base `Rectangle` class and a derived `Square` class (which inherits from `Rectangle`).

The application calculates basic geometric properties like area, perimeter, and diagonal length, provides a string representation of shapes, renders visual ASCII representations, and calculates how many times one shape can fit inside another.

---

## ✨ Features

- **Object-Oriented Design:** Clear inheritance structure between `Rectangle` and `Square`.
- **Geometric Calculations:** Instant computation of:
  - Area ($a = w \times h$)
  - Perimeter ($p = 2w + 2h$)
  - Diagonal ($d = \sqrt{w^2 + h^2}$)
- **ASCII Rendering:** Call `.get_picture()` to draw a visual representation of the shape using `*` characters.
- **Shape Nesting:** Use `.get_amount_inside(shape)` to calculate how many times a given shape fits inside another without rotation.
- **String Representations:** Custom `__str__` methods to output readable object descriptions (e.g., `Rectangle(width=10, height=5)`).

---

## 🚀 Getting Started

### Prerequisites

Make sure you have **Python 3.x** installed on your machine:
```bash
python --version
```

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/seanflaherty/polygon_area_calculator.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd polygon_area_calculator
   ```

---

## 💡 Usage Example

Below is a quick example demonstrating how to use the `Rectangle` and `Square` classes:

```python
from shape_calculator import Rectangle, Square

# Create a Rectangle instance
rect = Rectangle(10, 5)
print(rect.get_area())          # Output: 50
rect.set_height(3)
print(rect.get_perimeter())     # Output: 26
print(rect)                     # Output: Rectangle(width=10, height=3)
print(rect.get_picture())
# Output:
# **********
# **********
# **********

# Create a Square instance
sq = Square(9)
print(sq.get_area())            # Output: 81
sq.set_side(4)
print(sq.get_diagonal())        # Output: 5.656854249492381
print(sq)                       # Output: Square(side=4)

# Determine shape fitting
rect.set_width(16)
rect.set_height(8)
print(rect.get_amount_inside(sq)) # Output: 8
```

---

## 🧪 Testing

To run the test suite with **pytest**, execute:

```bash
pytest
```

---

## 🛠️ Built With

* **Language:** [Python 3](https://www.python.org/)
* **Testing:** [pytest](https://docs.pytest.org/)
* **Paradigm:** Object-Oriented Programming (OOP)

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for details.