"""
Script to calculate and print fibonacci sequence.  Defaulting to first 10.

Sample usage:
python fibonacci.py
python fibonacci.py -n 20
"""

from argparse import ArgumentParser
import sys


def fibonnaci(n):
    """
    Calculate the nth number of the Fibonacci sequence.

    :param n: position in the sequence in which to calculate.
    :return: int: nth number of the sequence.
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
        raise ValueError('Fibonnaci is defined only for n > 0.')


def main():
    parser = ArgumentParser()
    parser.add_argument('-n', '--n', type=int, required=False, default=10)
    args = parser.parse_args()

    fibonnaci_numbers = [fibonnaci(x) for x in range(args.n)]
    fibonnaci_sequence = ', '.join([str(f) for f in fibonnaci_numbers])
    print(fibonnaci_sequence)

    return 0


if __name__ == '__main__':
    sys.exit(main())
