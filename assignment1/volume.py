"""
Module for calculating volume of a cube.
"""


def volume(length):
    """
    Calculate volume of a cube.

    >>> volume(1)
    1

    >>> volume(10)
    1000

    >>> volume(3.14)
    30.959144000000002

    >>> volume()
    Traceback (most recent call last):
    ...
    TypeError: volume() missing 1 required positional argument: 'length'

    >>> volume('3')
    Traceback (most recent call last):
    ...
    TypeError: Volume can only be calculated for type int or float.

    >>> volume(0)
    Traceback (most recent call last):
    ...
    ValueError: Volume of a cube is only defined for length > 0.

    >>> volume(-1)
    Traceback (most recent call last):
    ...
    ValueError: Volume of a cube is only defined for length > 0.

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


if __name__ == '__main__':
    import doctest
    doctest.testmod()
