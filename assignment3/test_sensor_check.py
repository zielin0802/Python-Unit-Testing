"""Units tests for test_sensor_check.py.

Practicing testing with nose.
"""

import nose
from nose.tools import assert_false, assert_raises, assert_true, eq_, ok_
import unittest
from sensor_check import data_similar, humidity_in_range, seconds_in_range, temperature_in_range


def test_humidity_in_range_valid_inputs():
    """Test for humidity_in_range(). Valid input parameters."""
    assert not humidity_in_range(24)
    assert not humidity_in_range(24.001)
    assert humidity_in_range(25)
    assert humidity_in_range(30)
    assert humidity_in_range(40)
    assert not humidity_in_range(40.001)
    assert not humidity_in_range(41)


def test_humid_in_range_invalid_inputs():
    """Test for humidity_in_range(). Invalid input parameters."""
    assert_raises(TypeError, humidity_in_range, '40')


def test_seconds_in_range_valid_inputs():
    """Test for seconds_in_range(). Valid input parameters."""
    assert not seconds_in_range(9)
    assert not seconds_in_range(9.999999)
    assert seconds_in_range(10)
    assert seconds_in_range(15)
    assert seconds_in_range(20)
    assert not seconds_in_range(20.00001)
    assert not seconds_in_range(21)


def test_seconds_in_range_invalid_inputs():
    """Test for seconds_in_range(). Invalid input parameters."""
    assert_raises(TypeError, seconds_in_range, '15', 1, 10)


class TestSensorCheck(unittest.TestCase):
    """class definition for temperature_in_range() unit tests."""
    def test_temperature_in_range_valid_inputs(self):
        """Test for temperature_in_range(). Valid inputs."""
        self.assertFalse(temperature_in_range(temperature=59.999))
        self.assertTrue(temperature_in_range(temperature=60))
        self.assertTrue(temperature_in_range(temperature=80.2))
        self.assertTrue(temperature_in_range(temperature=90))
        self.assertFalse(temperature_in_range(temperature=90.001))

    def test_temperature_in_range_invalid_inputs(self):
        """Test for temperature_in_range(). Invalid inputs."""
        assert_raises(TypeError, temperature_in_range, '50')


def test_data_similar_valid_inputs():
    """Test for data_similar(). Valid inputs."""
    ok_(data_similar([80, 30], (80, 30)))
    eq_(data_similar([80, 30], (80, 40)), False)
    assert not data_similar([10, 20], [10, 30])
    assert_true(data_similar((1, 2), [1, 2]))
    assert_false(data_similar([1, 2, 3], [1, 2, 4]))


def test_data_similar_invalid_inputs():
    """Test for data_similar(). Invalid inputs."""
    assert_raises(ValueError, data_similar, [1, 2, 3], [1, 2])
    assert_raises(TypeError, data_similar, 5, [5])
    assert_raises(TypeError, data_similar, [1, 2], '1, 2')


if __name__ == '__main__':
    nose.run()
