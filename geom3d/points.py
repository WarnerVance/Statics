import math

from geom3d.vector import Vector
from geom3d.nums import are_close_enough

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def distance_to(self, other):
        delta_x = other.x - self.x
        delta_y = other.y - self.y
        delta_z = other.z - self.z
        return math.sqrt((delta_x ** 2) + (delta_y ** 2)+ (delta_z ** 2))
    def __sub__(self, other):
        return Vector(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )
    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, Point):
            return False
        return are_close_enough(self.x, other.x) and are_close_enough(self.y, other.y) and are_close_enough(self.z, other.z)
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    def displaced(self, vector: Vector, times=1):
        scaled_vec = vector.scaled_by(times)
        return Point(
            self.x + scaled_vec.i,
            self.y + scaled_vec.j,
            self.z + scaled_vec.k
        )
