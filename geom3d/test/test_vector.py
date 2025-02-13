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

    def test_vectorplusitself(self):
        a = Vector(1, 2, 3)
        assert a + a == Vector(2, 4, 6)
    def test_vectoradd(self):
        a = Vector(1, 2, 3)
        b = Vector(1, 2, 3)
        assert a + b == Vector(2, 4, 6)

class TestSubtract:

    def test_vectorminusitself(self):
        a = Vector(1, 2, 3)
        assert a - a == Vector(0, 0, 0)
    def test_vectorminus(self):
        a = Vector(1, 2, 3)
        b = Vector(1, 2, 3)
        assert a - b == Vector(0, 0, 0)

class TestNorm:
    def test_0vector(self):
        a = Vector(0, 0, 0)
        assert a.norm == 0
    def test_1vector(self):
        a = Vector(1, 0, 0)
        assert a.norm == 1
    def test_2dvector(self):
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

class Test_Scaled_by:
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
