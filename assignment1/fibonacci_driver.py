"""
Script to calculate and print fibonacci sequence.  Defaulting to first 10.

Sample usage:
python fibonacci.py
python fibonacci.py -n 20
"""

from argparse import ArgumentParser
import sys
from fibonacci import fibonacci


def main():
    parser = ArgumentParser()
    parser.add_argument('-n', '--n', type=int, required=False, default=10)
    args = parser.parse_args()

    fibonnaci_numbers = [fibonacci(x) for x in range(args.n)]
    fibonnaci_sequence = ', '.join([str(f) for f in fibonnaci_numbers])
    print(fibonnaci_sequence)

    return 0


if __name__ == '__main__':
    sys.exit(main())
