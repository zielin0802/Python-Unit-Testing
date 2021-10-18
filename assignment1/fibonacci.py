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

    >>> fibonacci('Lateralus')
    Traceback (most recent call last):
    ...
    TypeError: Fibonacci is defined only for type int.

    :param n: int: position in the sequence in which to calculate.
    :return int: nth number in the sequence.
    :raises TypeError: if n is not an integer
    :raises ValueError: if n < 0
    """
    if not isinstance(n, int):
        raise TypeError('Fibonacci is defined only for type int.')
    elif n < 0:
        raise ValueError('Fibonacci is defined only for n >= 0.')
    elif n in [0, 1]:
        return n
    else:
        fn2, fn1, fn = 0, 1, 1
        for _ in range(2, n + 1):
            fn = fn1 + fn2
            fn1, fn2 = fn, fn1
        return fn


def fibonacci_sequence(n):
    s = []
    if n == 0:
        s = [0]
    else:
        s = [0, 1]
        for i in range(2, n + 1):
            s.append(s[i - 1] + s[i - 2])
    return s


if __name__ == '__main__':
    from doctest import testmod
    testmod()
