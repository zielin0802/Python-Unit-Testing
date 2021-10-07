"""
Module to calculate Fibonacci to nth number in sequence.
"""


def fibonacci(n):
    """
    Calculate the nth number of the Fibonacci sequence.

    Examples:
    >>> fibonacci(0)
    0

    >>> fibonacci(1)
    1

    >>> fibonacci(9)
    34

    >>> [fibonacci(x) for x in range(10)]
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    >>> fibonacci(-1)
    Traceback (most recent call last):
    ...
    ValueError: Fibonacci is defined only for n >= 0.

    >>> fibonacci('5')
    Traceback (most recent call last):
    ...
    TypeError: Fibonacci is defined only for type int.

    :param n: position in the sequence in which to calculate.
    :return: int: how many numbers in the sequence to calculate.
    :raises: TypeError: if n is not an integer
    :raises: ValueError: if n < 0
    """
    if not isinstance(n, int):
        raise TypeError('Fibonacci is defined only for type int.')
    elif n in [0, 1]:
        return n
    elif n >= 2:
        Fn2, Fn1 = 0, 1
        for _ in range(2, n + 1):
            Fn = Fn1 + Fn2
            Fn1, Fn2 = Fn, Fn1
        return Fn
    else:
        raise ValueError('Fibonacci is defined only for n >= 0.')


if __name__ == '__main__':
    from doctest import testmod
    testmod()
