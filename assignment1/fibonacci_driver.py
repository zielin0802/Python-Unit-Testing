"""
Script to calculate and print fibonacci sequence.  Defaulting to first 10.

Sample usage:
python fibonacci_driver.py
python fibonacci_driver.py -n 20
"""

from argparse import ArgumentParser
import sys
from fibonacci import fibonacci_sequence


def main():
    parser = ArgumentParser()
    parser.add_argument('-n', '--n', type=int, required=False, default=10)
    args = parser.parse_args()

    sequence = fibonacci_sequence(args.n - 1)
    print(sequence)

    return 0


if __name__ == '__main__':
    sys.exit(main())
