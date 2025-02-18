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
        """
        Calculate and return the Euclidean norm (magnitude) of a vector.
        The norm is computed as the square root of the sum of the squared components.
        :return: The Euclidean norm of the vector.
        :rtype: float
        """
        return math.sqrt(self.i ** 2 + self.j ** 2 + self.k ** 2)

    def __str__(self):
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
        new vector that is perpendicular to both input vectors. This is often
        used in physics, computer graphics, and vector mathematics to determine
        the orientation of two vectors in three-dimensional space.

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
