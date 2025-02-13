from geom3d.nums import *


class TestAreCloseEnough:
    def test_numbers_close_enough_within_tolerance(self):
        assert are_close_enough(1.00000000001, 1.00000000002)

    def test_numbers_not_close_enough_outside_tolerance(self):
        assert not are_close_enough(1.0000001, 1.0000002)

    def test_numbers_exactly_equal(self):
        assert are_close_enough(1.0, 1.0)

    def test_numbers_negative_close_enough(self):
        assert are_close_enough(-1.00000000001, -1.00000000002)

    def test_numbers_positive_negative_close_enough(self):
        assert are_close_enough(0.00000000001, -0.00000000001)

    def test_numbers_positive_negative_not_close_enough(self):
        assert not are_close_enough(1.0, -1.0)

    def test_custom_tolerance_within(self):
        assert are_close_enough(1.0, 1.1, tolerance=0.2)

    def test_custom_tolerance_outside(self):
        assert not are_close_enough(1.0, 1.5, tolerance=0.2)

    def test_zero_close_to_zero(self):
        assert are_close_enough(0.0, 0.0)

    def test_large_numbers_close_enough(self):
        assert are_close_enough(1e10, 1e10 + 1e-5, tolerance=1e-4)


class TestIsCloseToZero:
    def test_positive_number_not_close_to_zero(self):
        assert not is_close_to_zero(1.0)

    def test_negative_number_not_close_to_zero(self):
        assert not is_close_to_zero(-1.0)

    def test_small_positive_number_close_to_zero(self):
        assert is_close_to_zero(1e-11)

    def test_small_negative_number_close_to_zero(self):
        assert is_close_to_zero(-1e-11)

    def test_number_equal_to_zero(self):
        assert is_close_to_zero(0.0)

    def test_number_within_custom_tolerance_close_to_zero(self):
        assert is_close_to_zero(5e-5, tolerance=1e-4)

    def test_number_outside_custom_tolerance_not_close_to_zero(self):
        assert not is_close_to_zero(5e-5, tolerance=1e-6)

    def test_large_positive_number_not_close_to_zero(self):
        assert not is_close_to_zero(1e6)

    def test_large_negative_number_not_close_to_zero(self):
        assert not is_close_to_zero(-1e6)


class TestIsCloseToOne:
    def test_number_exactly_one(self):
        assert is_close_to_one(1.0)

    def test_number_close_to_one_positive(self):
        assert is_close_to_one(1.00000000001)

    def test_number_close_to_one_negative(self):
        assert is_close_to_one(0.99999999999)

    def test_number_not_close_to_one_positive(self):
        assert not is_close_to_one(1.0001)

    def test_number_not_close_to_one_negative(self):
        assert not is_close_to_one(0.9999)

    def test_custom_tolerance_within(self):
        assert is_close_to_one(1.001, tolerance=0.01)

    def test_custom_tolerance_outside(self):
        assert not is_close_to_one(1.01, tolerance=0.001)

    def test_zero_not_close_to_one(self):
        assert not is_close_to_one(0.0)

    def test_large_number_not_close_to_one(self):
        assert not is_close_to_one(1000000.0)

    def test_negative_large_number_not_close_to_one(self):
        assert not is_close_to_one(-1000000.0)

    def test_nearby_negative_number_not_close_to_one(self):
        assert not is_close_to_one(-0.9999)
