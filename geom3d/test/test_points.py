import math

from geom3d.nums import are_close_enough
from geom3d.points import Point
from geom3d.vector import Vector


def test_init():
    a = Point(1,2,3)
    assert True

class TestDistanceTo:
    def test_distance_to_same_point(self):
        a = Point(1, 2, 3)
        assert a.distance_to(a) == 0

    def test_distance_to_different_points(self):
        p1 = Point(0, 0, 0)
        p2 = Point(3, 4, 0)
        expected_distance = math.sqrt((3 ** 2) + (4 ** 2) + (0 ** 2))
        assert are_close_enough(
            p1.distance_to(p2),
            expected_distance)


    def test_distance_to_negative_coordinates(self):
        p1 = Point(-1, -2, -3)
        p2 = Point(-4, -6, -8)
        expected_distance = math.sqrt((3 ** 2) + (4 ** 2) + (5 ** 2))
        assert are_close_enough(
            p1.distance_to(p2),
            expected_distance)


    def test_distance_to_fractional_coordinates(self):
        p1 = Point(1.5, 2.5, 3.5)
        p2 = Point(4.5, 6.5, 8.5)
        expected_distance = math.sqrt((3.0 ** 2) + (4.0 ** 2) + (5.0 ** 2))
        assert are_close_enough(p1.distance_to(p2), expected_distance)

class TestSubtraction:
    def test_subtract_two_points(self):
        p1 = Point(1, 2, 3)
        p2 = Point(4, 5, 6)
        result = p1 - p2
        assert isinstance(result, Vector)
        assert result.i == -3
        assert result.j == -3
        assert result.k == -3

    def test_subtract_point_from_itself(self):
        p = Point(1, 2, 3)
        result = p - p
        assert isinstance(result, Vector)
        assert result.i == 0
        assert result.j == 0
        assert result.k == 0

    def test_subtract_negative_coordinates(self):
        p1 = Point(-1, -2, -3)
        p2 = Point(-4, -5, -6)
        result = p1 - p2
        assert isinstance(result, Vector)
        assert result.i == 3
        assert result.j == 3
        assert result.k == 3

    def test_subtract_mixed_coordinates(self):
        p1 = Point(1, -2, 3)
        p2 = Point(-4, 5, 6)
        result = p1 - p2
        assert isinstance(result, Vector)
        assert result.i == 5
        assert result.j == -7
        assert result.k == -3

class TestPointEquality:
    def test_same_instance(self):
        p = Point(1.0, 2.0, 3.0)
        assert p == p

    def test_equal_points(self):
        p1 = Point(1.0, 2.0, 3.0)
        p2 = Point(1.0, 2.0, 3.0)
        assert p1 == p2

    def test_not_equal_points(self):
        p1 = Point(1.0, 2.0, 3.0)
        p2 = Point(4.0, 5.0, 6.0)
        assert p1 != p2

    def test_not_equal_different_type(self):
        p = Point(1.0, 2.0, 3.0)
        other = (1.0, 2.0, 3.0)  # not a Point instance
        assert p != other

    def test_close_enough_points(self):
        p1 = Point(1.00000000000001, 2.00000000000001, 3.00000000000001)
        p2 = Point(1.00000000000002, 2.00000000000002, 3.00000000000002)
        assert p1 == p2

    def test_far_apart_points(self):
        p1 = Point(1.0, 1.0, 1.0)
        p2 = Point(1.01, 1.01, 1.01)
        assert p1 != p2

class TestPointStr:
    def test_str_origin(self):
        p = Point(0, 0, 0)
        assert str(p) == "(0, 0, 0)"

    def test_str_positive_coordinates(self):
        p = Point(1, 2, 3)
        assert str(p) == "(1, 2, 3)"

    def test_str_negative_coordinates(self):
        p = Point(-1, -2, -3)
        assert str(p) == "(-1, -2, -3)"

    def test_str_mixed_coordinates(self):
        p = Point(1, -2, 3)
        assert str(p) == "(1, -2, 3)"

    def test_str_floating_point_coordinates(self):
        p = Point(1.5, 0.25, -3.4)
        assert str(p) == "(1.5, 0.25, -3.4)"


class TestPoint:
    def test_distance_to_same_point(self):
        p1 = Point(1.0, 2.0, 3.0)
        assert p1.distance_to(p1) == 0.0

    def test_distance_to_different_point(self):
        p1 = Point(0.0, 0.0, 0.0)
        p2 = Point(3.0, 4.0, 0.0)
        assert p1.distance_to(p2) == 5.0

    def test_subtraction_between_points(self):
        p1 = Point(5.0, 7.0, 9.0)
        p2 = Point(2.0, 3.0, 4.0)
        result = p1 - p2
        assert result.i == 3.0
        assert result.j == 4.0
        assert result.k == 5.0

    def test_equality_same_point(self):
        p1 = Point(1.0, 2.0, 3.0)
        p2 = Point(1.0, 2.0, 3.0)
        assert p1 == p2

    def test_equality_within_tolerance(self):
        p1 = Point(1.000000000001, 2.000000000001, 3.00000000001)
        p2 = Point(1.0, 2.0, 3.0)
        assert p1 == p2

    def test_equality_different_points(self):
        p1 = Point(1.0, 2.0, 3.0)
        p2 = Point(4.0, 5.0, 6.0)
        assert p1 != p2

    def test_str_representation(self):
        p = Point(1.234, 5.678, 9.1011)
        assert str(p) == "(1.234, 5.678, 9.1011)"

    def test_displaced_point_without_scaling(self):
        p = Point(1.0, 2.0, 3.0)
        v = Vector(1.0, 1.0, 1.0)
        displaced = p.displaced(v)
        assert displaced == Point(2.0, 3.0, 4.0)

    def test_displaced_point_with_scaling(self):
        p = Point(1.0, 1.0, 1.0)
        v = Vector(2.0, 3.0, 4.0)
        displaced = p.displaced(v, times=2)
        assert displaced == Point(5.0, 7.0, 9.0)


class TestMakeVector:
    def test_make_vector_valid(self):
        p1 = Point(1, 2, 3)
        p2 = Point(4, 5, 6)
        result = p1.make_vector(p2)
        expected = Vector(3, 3, 3)
        assert result == expected

    def test_make_vector_zero_difference(self):
        p1 = Point(1, 1, 1)
        p2 = Point(1, 1, 1)
        result = p1.make_vector(p2)
        expected = Vector(0, 0, 0)
        assert result == expected

    def test_make_vector_negative_coordinates(self):
        p1 = Point(-1, -2, -3)
        p2 = Point(-4, -5, -6)
        result = p1.make_vector(p2)
        expected = Vector(-3, -3, -3)
        assert result == expected

    def test_make_vector_mixed_coordinates(self):
        p1 = Point(1, -2, 3)
        p2 = Point(-4, 5, -6)
        result = p1.make_vector(p2)
        expected = Vector(-5, 7, -9)
        assert result == expected

    def test_make_vector_to_point_at_origin(self):
        p1 = Point(1, 2, 3)
        p2 = Point(0, 0, 0)
        result = p1.make_vector(p2)
        expected = Vector(-1, -2, -3)
        assert result == expected
