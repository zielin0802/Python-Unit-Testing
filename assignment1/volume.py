"""
Module for calculating volume of a cube.
"""


def volume(x):
    """
    Calculate volume of a cube.

    :param x: (int, float): length of one side of the cube
    :return: (int, float): volume of the cube.
    :raises TypeError: if x is not an int or float
    :raises ValueError: if x <= 0
    """
    if not isinstance(x, (int, float)):
        raise TypeError('Volume can only be calculated for type int or float.')
    if x <= 0:
        raise ValueError('Volume is only defined for x > 0.')
    return x ** 3
