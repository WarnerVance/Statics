import math

def are_close_enough(a, b, tolerance=1e-10):
    """
    Determines if two floating-point numbers are close enough to each other
    based on a specified tolerance.

    This function calculates the absolute difference between two input numbers
    and compares it to a defined tolerance. It returns a boolean indicating
    whether the difference falls within the tolerance range.

    :param a: The first floating-point number to compare.
    :type a: float
    :param b: The second floating-point number to compare.
    :type b: float
    :param tolerance: The acceptable difference between a and b for them to be
        considered close enough. Defaults to 1e-10.
    :type tolerance: float
    :return: A boolean indicating whether the absolute difference of the
        numbers is less than the specified tolerance.
    :rtype: bool
    """
    return math.fabs(a-b) < tolerance

def is_close_to_zero(a, tolerance=1e-10):
    """
    Determines whether a given number is close to zero, within a specified
    tolerance. The comparison uses absolute difference to check proximity
    to zero.

    :param a: The number to be checked for closeness to zero.
    :type a: float
    :param tolerance: The maximum acceptable difference from zero to
        consider the number as close. Defaults to 1e-10.
    :type tolerance: float, optional
    :return: A boolean indicating whether the number is close to zero.
    :rtype: bool
    """
    return are_close_enough(a, 0.0, tolerance)

def is_close_to_one(a, tolerance=1e-10):
    """
    Determines if a given number is close to 1.0 within a specified tolerance.

    This function checks if the input value `a` is approximately equal to 1.0,
    considering a margin specified by `tolerance`. It uses a helper function
    to perform the comparison.

    :param a: The number to check for closeness to 1.0.
    :type a: float
    :param tolerance: The acceptable deviation from 1.0 for the check. Defaults to 1e-10.
    :type tolerance: float, optional
    :return: True if the number `a` is close to 1.0 within the allowed tolerance, False otherwise.
    :rtype: bool
    """
    return are_close_enough(a, 1.0, tolerance)