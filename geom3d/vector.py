import math

from geom3d.nums import are_close_enough
from geom3d.nums import is_close_to_zero


class Vector:
    def __init__(self, i, j, k):
        """
        Initialize the example class with given parameters `i`, `j`, and `k`.

        :param i: Represents the first parameter of the class. Should be an integer.
        :param j: Represents the second parameter of the class. Should be a string value.
        :param k: Represents the third parameter of the class. Should be a float.

        """
        self.i = i
        self.j = j
        self.k = k

    def __eq__(self, other):
        """
        Compares the current Vector instance with another object to determine
        if they are equal. The method checks for reference equality first,
        then for type compatibility. If the types match, it performs a
        component-wise comparison using the `are_close_enough` function to
        determine if the components of the two vectors are sufficiently
        close to be considered equal.

        :param other: The object to compare with the current instance.
                      Should be of type `Vector`.
        :type other: Any
        :return: True if the current instance is equal to the object
                 specified, False otherwise.
        :rtype: bool
        """
        if self is other:
            return True
        if not isinstance(other, Vector):
            return False
        return are_close_enough(self.i, other.i) and are_close_enough(self.j, other.j) and are_close_enough(self.k,
                                                                                                            other.k)

    def __add__(self, other):
        """
        Adds two vectors together to return a new vector. The operation is only valid when both
        operands are instances of the Vector class. If the operand is not a Vector, the method
        returns a string indicating that the operation cannot be performed.

        :param other: The Vector instance to be added to the current Vector instance.
        :return: A new Vector instance representing the result of the vector addition,
            or a string indicating an invalid operation if `other` is not a Vector.
        """
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
        """
        Calculate and return the Euclidean norm (magnitude) of a vector.
        The norm is computed as the square root of the sum of the squared components.
        :return: The Euclidean norm of the vector.
        :rtype: float
        """
        return math.sqrt(self.i ** 2 + self.j ** 2 + self.k ** 2)

    def __str__(self):
        """
        Converts the current instance of the class to its string representation.

        The method provides a formatted string representing
        the object including its attributes and computed properties.
        It is intended to make the object more human-readable.

        :return: A string representation of the object, including its attributes and
            a computed property `norm`.
        :rtype: str
        """
        return f"({self.i}, {self.j}, {self.k}) with norm {self.norm}"

    def scaled_by(self, factor):
        """
        Scales the vector by a given factor.

        This method multiplies each component of the vector
        (i, j, k) by the specified factor to produce a scaled
        vector. It returns a new Vector instance with scaled
        components.

        :param factor: The factor by which to scale the vector.
        :type factor: float or int
        :return: A new Vector instance with components scaled
            by the given factor.
        :rtype: Vector
        """
        return Vector(
            self.i * factor,
            self.j * factor,
            self.k * factor
        )

    def __mul__(self, other):
        """
        Implements the multiplication operation for the class. Allows objects of the
        class to be scaled by another value through multiplication, invoking the
        `scaled_by` method of the class. It returns a new instance with the modified
        values resulting from the scaling operation.

        :param other: The value used to scale the current object.
        :type other: float or int
        :return: A new Vector instance with scaled components.
        """
        return self.scaled_by(other)

    def dot(self, other):
        """
        Computes the dot product of this vector with another vector.

        The dot product is a scalar value that is the sum of the products
        of the corresponding components of the two vectors. This operation
        takes two 3-dimensional vectors (self and other) and computes their
        dot product.

        :param other: Another vector with which the dot product is to be
            computed.
        :type other: Vector
        :return: The dot product of the two vectors. It represents the
            scalar value resulting from the dot product calculation.
        :rtype: float
        """
        return self.i * other.i + self.j * other.j + self.k * other.k

    def cross(self, other):
        """
        Computes the cross product of the current vector with another vector.

        The cross product is performed between two 3D vectors and results in a
        new vector that is perpendicular to both input vectors.

        :param other: The other vector to compute the cross product with.
        :type other: Vector
        :return: A new vector that is the result of the cross product operation.
        :rtype: Vector
        """
        return Vector(
            self.j * other.k - self.k * other.j,
            self.k * other.i - self.i * other.k,
            self.i * other.j - self.j * other.i
        )

    @property
    def unit(self):
        """
        Computes the unit (normalized) vector of the current vector.

        If the norm of the vector is close to zero, it returns the vector itself to avoid
        division by zero. Otherwise, it calculates the unit vector by scaling the current
        vector using the inverse of its norm.

        :rtype: Vector
        :return: The unit vector if the norm is not zero, or the vector itself if the norm is zero.
        """
        if are_close_enough(self.norm, 0):
            # This allows for the special case were we try to find the unit vector of the
            # zero vector. This would involve dividing by zero so we need another bit of logic to handle that
            return self
        return self.scaled_by(1 / self.norm)

    def comp(self, other):
        """
        This computes the scalar projection of self over other.

        :param other: The vector instance with which comparison is made.
        :type other: Vector
        :return: The ratio of the dot product of this vector and `other` to the
            norm of `other`.
        :rtype: float
        """
        return self.dot(other) / other.norm

    def is_parallel(self, other):
        """
        Determines whether the current vector is parallel to another vector.

        This method checks if the cross product of the two vectors is equal
        to the zero vector, which indicates parallelism. A vector is parallel
        to another if they lie in the same or opposite direction along the
        same line but differ only in magnitude or direction. A zero vector is parrallel to any vector.

        :param other: The other vector to compare.
        :type other: Vector
        :return: True if the vectors are parallel, False otherwise.
        :rtype: bool
        """
        return is_close_to_zero(self.cross(other).norm)

    def make_length(self, length: int or float):
        """
        This function makes a vector have a given length while preserving it's direction.
        It does this by first finding the unit vector and then scaling it by the given length.

        :param length: The value by which the current unit will be scaled. It can
                      be either `int` or `float`.
        :type length: int or float
        :return: A vector with the given length
        :rtype: Vector

        """
        if self == Vector(0, 0, 0):
            return Vector(0, 0, 0)
        return self.unit.scaled_by(length)

    def find_angle(self, other, plane=1):
        """

        :param other: The other vector
        :type other: Vector
        :param plane: 1 for xy, 2 for xz, 3 for yz
        :return: The angle between the two vectors in degrees
        :rtype: float
        """
        # Find what plane we're talking about here
        # xy xz or yz
        # We will ignore the other coordinate
