"""
Module for calculating volume of a cube.
"""


def volume(length):
    """
    Calculate volume of a cube.

    :param length: (int | float): length of one side of the cube
    :return: (int | float): volume of the cube.
    :raises TypeError: if length is not an int or float
    :raises ValueError: if length <= 0
    """
    if not isinstance(length, (int, float)):
        raise TypeError('Volume can only be calculated for type int or float.')
    if length <= 0:
        raise ValueError('Volume of a cube is only defined for length > 0.')
    return length ** 3
