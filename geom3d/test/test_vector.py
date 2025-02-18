import pytest

from geom3d.nums import are_close_enough
from geom3d.vector import Vector


def test_init():
    a = Vector(1, 2, 3)
    assert True
class TestEqual:

    def test_same(self):
        a = Vector(1, 2, 3)
        assert a == a

    def test_duplicate(self):
        a = Vector(1, 2, 3)
        b = Vector(1, 2, 3)
        assert a == b

    def test_different_vectors(self):
        a = Vector(1, 2, 3)
        b = Vector(1, 3, 3)
        assert a != b

    def test_different_types(self):
        a = Vector(1, 2, 3)
        b = 4
        assert a != b
        b = "4"
        assert a != b
        b = 4.1
        assert a != b

class TestAdd:

    def test_vector_plus_itself(self):
        a = Vector(1, 2, 3)
        assert a + a == Vector(2, 4, 6)
    def test_vector_add(self):
        a = Vector(1, 2, 3)
        b = Vector(1, 2, 3)
        assert a + b == Vector(2, 4, 6)

    def test_vector_add_int(self):
        a = Vector(1, 2, 3)
        b = 1
        assert (a + b) == "You can't do that"

class TestSubtract:

    def test_vector_minus_itself(self):
        a = Vector(1, 2, 3)
        assert a - a == Vector(0, 0, 0)
    def test_vector_minus(self):
        a = Vector(1, 2, 3)
        b = Vector(1, 2, 3)
        assert a - b == Vector(0, 0, 0)

class TestNorm:
    def test_0_vector(self):
        a = Vector(0, 0, 0)
        assert a.norm == 0
    def test_1_vector(self):
        a = Vector(1, 0, 0)
        assert a.norm == 1
    def test_2d_vector(self):
        a = Vector(1, 1, 0)
        assert are_close_enough(
            a.norm,
            1.4142135623730951)
    def test_3vector(self):
        a = Vector(1, 1, 1)
        assert are_close_enough(a.norm, 3 ** 0.5)


def test_string():
    a = Vector(1, 2, 3)
    norm = a.norm
    assert str(a) == "(1, 2, 3) with norm " + str(norm)

class TestScaledBy:
    def test_scale_by_1(self):
        a = Vector(1, 2, 3)
        assert a.scaled_by(1) == a
    def test_scale_by_2(self):
        a = Vector(1, 2, 3)
        assert a.scaled_by(2) == Vector(2, 4, 6)
    def test_scale_by_0(self):
        a = Vector(1, 2, 3)
        assert a.scaled_by(0) == Vector(0, 0, 0)
    def test_scale_by_negative(self):
        a = Vector(1, 2, 3)
        assert a.scaled_by(-1) == Vector(-1, -2, -3)

class TestMul:
    def test_scale_by_1(self):
        a = Vector(1, 2, 3)
        assert a * 1 == a

    def test_scale_by_2(self):
        a = Vector(1, 2, 3)
        assert a *2 == Vector(2, 4, 6)

    def test_scale_by_0(self):
        a = Vector(1, 2, 3)
        assert a * 0 == Vector(0, 0, 0)

    def test_scale_by_negative(self):
        a = Vector(1, 2, 3)
        assert a * -1 == Vector(-1, -2, -3)

class TestDot:
    def test_dot_self(self):
        a = Vector(1, 2, 3)
        assert a.dot(a) == 14
    def test_perpendicular(self):
        a = Vector(1,0,0)
        b = Vector(0,1,0)
        assert a.dot(b) == 0
    def test_parallel(self):
        a = Vector(1, 0, 0)
        b = Vector(2, 0, 0)
        assert a.dot(b) == 2

class TestCross:
    def test_unit_perp(self):
        a = Vector(1, 0, 0)
        b = Vector(0, 1, 0)
        assert a.cross(b) == Vector(0, 0, 1)
    def test_perp(self):
        a = Vector(2, 0, 0)
        b = Vector(0, 2, 0)
        print(str(a.cross(b)))
        assert a.cross(b) == Vector(0, 0, 4)
    def test_general(self):
        a = Vector(1, 2, 3)
        b = Vector(4, 5, 6)
        assert a.cross(b) == Vector(-3, 6, -3)

class TestUnit:
    def test_vector_to_unit(self):
        a = Vector(1, 2, 3)
        assert are_close_enough(0.2672612419, a.unit.i)
        assert are_close_enough(0.5345224838, a.unit.j)
        assert are_close_enough(0.8017837257, a.unit.k)
    def test_unit_to_unit(self):
        a = Vector(1, 0, 0)
        assert a.unit == a
    def test_zero_vector(self):
        a = Vector(0, 0, 0)
        assert a.unit == Vector(0, 0, 0)
    def test_norm(self):
        a = Vector(5,3,8)
        a = a.unit
        assert are_close_enough(a.norm,1 )


class TestComp:

    def test_comp_orthogonal_vectors(self):
        v1 = Vector(1, 0, 0)
        v2 = Vector(0, 1, 0)
        assert v1.comp(v2) == 0

    def test_comp_parallel_unit_vectors(self):
        v1 = Vector(1, 0, 0)
        v2 = Vector(1, 0, 0)
        assert v1.comp(v2) == 1

    def test_comp_parallel_non_unit_vectors(self):
        v1 = Vector(2, 0, 0)
        v2 = Vector(4, 0, 0)
        assert v1.comp(v2) == pytest.approx(2)

    def test_comp_negative_component(self):
        v1 = Vector(-2, 0, 0)
        v2 = Vector(0, -3, 0)
        assert v1.comp(v2) == 0

    def test_comp_with_non_zero_result(self):
        v1 = Vector(3, 4, 0)
        v2 = Vector(6, 8, 0)
        assert v1.comp(v2) == pytest.approx(5)

    def test_comp_small_vectors(self):
        v1 = Vector(0.001, 0.002, 0.003)
        v2 = Vector(0.004, 0.005, 0.006)
        assert v1.comp(v2) == pytest.approx(0.003646738446708415)

    def test_comp_with_zero_vector(self):
        v1 = Vector(1, 2, 3)
        v2 = Vector(0, 0, 0)
        with pytest.raises(ZeroDivisionError):
            v1.comp(v2)
