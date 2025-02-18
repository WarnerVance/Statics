import math

from geom3d.nums import are_close_enough
from geom3d.vector import Vector


class Point:
    def __init__(self, x, y, z):
        """
        Represents a class that encapsulates three attributes `x`, `y`, and `z`.

        This class is designed to initialize its attributes using the parameters
        passed to the constructor. The class does not implement any additional
        methods or behavior aside from storing the data.


        :param x: The value to be stored in the `x` attribute.
        :type x: float or int
        :param y: The value to be stored in the `y` attribute.
        :type y: float or int
        :param z: The value to be stored in the `z` attribute.
        :type z: float or int
        """
        self.x = x
        self.y = y
        self.z = z

    def distance_to(self, other):
        """
        Calculates the Euclidean distance from the current point to another point in 3D space.

        The method computes the straight-line distance between two points in a three-dimensional
        coordinate space (x, y, z). It follows the formula:

            distance sqrt((x2 - x1)^2 + (y2 - y1)^2 + (z2 - z1)^2)

        :param other: The other point to calculate the distance to.
        :type other: Point
        :return: The Euclidean distance between the two points.
        :rtype: float
        """
        delta_x = other.x - self.x
        delta_y = other.y - self.y
        delta_z = other.z - self.z
        return math.sqrt((delta_x ** 2) + (delta_y ** 2) + (delta_z ** 2))

    def __sub__(self, other):
        """
        Performs subtraction of two vectors.

        This method calculates the difference between two vectors
        component-wise and returns a new vector representing the result.

        :param other: The vector to subtract from this vector.
        :type other: Vector
        :return: A new vector which is the result of the subtraction.
        :rtype: Vector
        """
        return Vector(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )

    def __eq__(self, other):
        """
        Compares two Point objects for equality.

        The method determines if the current Point object is equivalent to another
        object by checking reference equality. If the objects are not the same reference,
        it verifies they are both instances of the Point class. Finally, it compares
        the x, y, and z attributes of both objects using a precision function
        `are_close_enough`.

        :param other: The object to compare with the current Point instance.
        :type other: Point
        :return: True if the objects are equal, False otherwise.
        :rtype: bool
        """
        if self is other:
            return True
        if not isinstance(other, Point):
            return False
        return are_close_enough(self.x, other.x) and are_close_enough(self.y, other.y) and are_close_enough(self.z,
                                                                                                            other.z)

    def __str__(self):
        """
        Represents an object by converting it into a string.

        This method provides a textual representation of the object, specifically a
        formatted string containing the attributes of the instance. It is executed
        when `str()` is called on the object or it is used in a string context.

        :return: A formatted string representing the object attributes.
        :rtype: str
        """
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
        :type times: int or float
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
        :type other: Point
        :return: A new vector instance representing the difference between
            the current instance and the `other` instance.
        :rtype: Vector
        """
        return Vector(
            other.x - self.x,
            other.y - self.y,
            other.z - self.z
        )
