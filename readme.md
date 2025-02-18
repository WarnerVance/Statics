# Statics Tools

This project provides a set of classes and utilities for performing operations in 3D geometry, such as working with
vectors, points, and mathematical computations.

## Features

- **Vector Operations**:
    - Creation of 3D vectors with `i`, `j`, `k` components.
    - Support for vector addition, subtraction, scalar multiplication, dot and cross products.
    - Compute vector magnitude (norm) and unit vectors.
    - Scaling vectors and projecting vectors.

- **Point Operations**:
    - Calculate distances between points in 3D space.
    - Displacement of points based on vectors.
    - Point comparisons and vector creation from points.

- **Numeric Utilities**:
    - Functions to verify closeness of floating-point numbers with a defined tolerance.
    - Check if a value is close to zero or one using customizable tolerances.

## Installation

To use these utilities in your Python project:

1. Clone the repository.

``` bash
   git clone https://github.com/WarnerVance/Statics.git
```

2.(Optional) Set up a virtual environment.

``` bash
   python -m venv venv
   source venv/bin/activate # For Linux/MacOS
   venv\Scripts\activate    # For Windows
```

1. Install dependencies.

``` bash
   pip install pytest
```

## Usage

Below are example use cases for the project:

### Vectors

``` python
from geom3d.vector import Vector

# Create vectors
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Add vectors
v3 = v1 + v2

# Cross product
cross_product = v1.cross(v2)

# Get unit vector
unit_vector = v1.unit()
```

### Points

``` python
from geom3d.points import Point

# Create points
p1 = Point(1, 2, 3)
p2 = Point(4, 5, 6)

# Compute distance
distance = p1.distance_to(p2)

# Create a vector from two points
vector = p1.make_vector(p2)

# Displace a point
displaced_point = p1.displaced(vector, times=2)
```

### Numeric Utilities

This helps make up for float point math precision problems.

``` python
from geom3d.nums import are_close_enough, is_close_to_zero

# Compare floating-point numbers
result = are_close_enough(0.1 + 0.2, 0.3)

# Check if a value is close to zero
zero_check = is_close_to_zero(1e-11)
```

## Structure

- **`vector.py` **: Implements the `Vector` class with methods for 3D vector computations.
- **`points.py` **: Implements the `Point` class to represent points in 3D space and associated methods.
- **`nums.py` **: Provides helper functions for floating-point number comparisons with tolerances.

If you'd like me to expand or focus on a specific section, let me know! 😊
