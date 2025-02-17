import math

from geom3d.nums import are_close_enough
from geom3d.vector import Vector


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance_to(self, other):
        delta_x = other.x - self.x
        delta_y = other.y - self.y
        delta_z = other.z - self.z
        return math.sqrt((delta_x ** 2) + (delta_y ** 2) + (delta_z ** 2))

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
        return are_close_enough(self.x, other.x) and are_close_enough(self.y, other.y) and are_close_enough(self.z,
                                                                                                            other.z)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def displaced(self, vector: Vector, times=1):
        """
        Displaces the current point by a scaled vector.

        This method creates a new point by moving the current point along a given vector,
        scaled by a specified factor. The scaling is performed by the method
        `scaled_by` from the `Vector` class. The translated point is then calculated
        and returned as a new `Point` object.

        :param vector: The vector along which the point should be displaced.
            This vector defines the direction of the movement.
        :type vector: Vector
        :param times: An optional scale factor used to modify the vector's magnitude
            before displacing the point. By default, it is set to 1.
        :type times: int
        :return: A new `Point` object representing the displaced point.
        :rtype: Point
        """
        scaled_vec = vector.scaled_by(times)
        return Point(
            self.x + scaled_vec.i,
            self.y + scaled_vec.j,
            self.z + scaled_vec.k
        )

    def make_vector(self, other):
        """
        Computes a vector between the current instance and another point
        in a 3-dimensional space. The resulting vector is determined by
        subtracting the coordinates of the current instance from the
        corresponding coordinates of the `other` instance. The vector is from
        self and to other.

        :param other: An instance representing a 3D point with `x`, `y`,
            and `z` attributes.
        :type other: Vector
        :return: A new vector instance representing the difference between
            the current instance and the `other` instance.
        :rtype: Vector
        """
        return Vector(
            other.x - self.x,
            other.y - self.y,
            other.z - self.z
        )
