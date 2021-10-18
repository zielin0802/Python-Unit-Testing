"""
Unit test script for fibonacci.py.
"""

import unittest
from fibonacci import fibonacci


class Testfibonacci(unittest.TestCase):
    def test_fibonacci_invalid_input(self):
        """Test for fibonacci().  Invalid inputs."""
        with self.assertRaises(ValueError):
            fibonacci(-1)
        with self.assertRaises(TypeError):
            fibonacci('Lateralus')
        with self.assertRaises(TypeError):
            fibonacci(None)
        with self.assertRaises(TypeError):
            fibonacci(3.0)

    def test_fibonacci_valid_input(self):
        """Test for fibonacci().  Valid inputs."""
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(7), 13)
        self.assertEqual(fibonacci(8), 21)
        self.assertEqual(fibonacci(9), 34)
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(11), 89)
        self.assertEqual(fibonacci(12), 144)
        self.assertEqual(fibonacci(13), 233)


if __name__ == '__main__':
    unittest.main()
