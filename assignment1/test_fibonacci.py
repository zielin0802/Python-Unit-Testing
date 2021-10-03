"""
Unit test script for fibonnaci.py.
"""

import unittest
from fibonacci import fibonnaci


class TestFibonnaci(unittest.TestCase):
    def test_fibonnaci_invalid_input(self):
        """Test for fibonnaci().  Invalid inputs."""
        with self.assertRaises(ValueError):
            fibonnaci(-1)
        with self.assertRaises(TypeError):
            fibonnaci('1')
        with self.assertRaises(TypeError):
            fibonnaci(None)
        with self.assertRaises(TypeError):
            fibonnaci(3.0)

    def test_fibonnaci_valid_input(self):
        """Test for fibonnaci().  Valid inputs."""
        self.assertEqual(fibonnaci(0), 0)
        self.assertEqual(fibonnaci(1), 1)
        self.assertEqual(fibonnaci(2), 1)
        self.assertEqual(fibonnaci(3), 2)
        self.assertEqual(fibonnaci(4), 3)
        self.assertEqual(fibonnaci(5), 5)
        self.assertEqual(fibonnaci(6), 8)
        self.assertEqual(fibonnaci(7), 13)
        self.assertEqual(fibonnaci(8), 21)
        self.assertEqual(fibonnaci(9), 34)
        self.assertEqual(fibonnaci(10), 55)
        self.assertEqual(fibonnaci(11), 89)


if __name__ == '__main__':
    unittest.main()
