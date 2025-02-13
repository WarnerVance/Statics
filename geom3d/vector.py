import math

from geom3d.nums import are_close_enough


class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, Vector):
            return False
        return are_close_enough(self.i, other.i) and are_close_enough(self.j, other.j) and are_close_enough(self.k,
                                                                                                            other.k)

    def __add__(self, other):
        if not isinstance(other, Vector):
            return "You can't do that"
        return Vector(
            self.i + other.i,
            self.j + other.j,
            self.k + other.k
        )

    def __sub__(self, other):
        return Vector(
            self.i - other.i,
            self.j - other.j,
            self.k - other.k
        )

    @property
    def norm(self):
        return math.sqrt(self.i ** 2 + self.j ** 2 + self.k ** 2)

    def __str__(self):
        return f"({self.i}, {self.j}, {self.k}) with norm {self.norm}"

    def scaled_by(self, factor):
        return Vector(
            self.i * factor,
            self.j * factor,
            self.k * factor
        )

    def __mul__(self, other):
        return self.scaled_by(other)



    def dot(self, other):
        return self.i * other.i + self.j * other.j + self.k * other.k

    def cross(self, other):
        return Vector(
            self.j * other.k - self.k * other.j,
            self.k * other.i - self.i * other.k,
            self.i * other.j - self.j * other.i
        )

    @property
    def unit(self):
        if are_close_enough(self.norm, 0):
            return self
        return self.scaled_by(1 / self.norm)
