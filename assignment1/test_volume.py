"""
Unit test script for volume.py.
"""

import math
import unittest
from volume import volume


class TestVolume(unittest.TestCase):
    def test_volume_invalid_input(self):
        """Test for volume().  Invalid inputs."""
        with self.assertRaises(ValueError):
            volume(0)
        with self.assertRaises(ValueError):
            volume(-1)
        with self.assertRaises(ValueError):
            volume(-0.000001)
        with self.assertRaises(TypeError):
            volume(None)
        with self.assertRaises(TypeError):
            volume('3')
        with self.assertRaises(TypeError):
            volume(complex(1, 2))
        with self.assertRaises(TypeError):
            volume(4 - 2j)

    def test_volume_valid_input(self):
        """Test for volume().  Valid inputs."""
        self.assertEqual(volume(1), 1)
        self.assertEqual(volume(2), 8)
        self.assertEqual(volume(3), 27)
        self.assertEqual(volume(4), 64)
        self.assertEqual(volume(0.001), 1e-9)
        self.assertAlmostEqual(volume(1.1), 1.331)
        self.assertAlmostEqual(volume(math.pi), 31.006276680299)
        self.assertAlmostEqual(volume(math.e), 20.085536923187)


if __name__ == '__main__':
    unittest.main()
