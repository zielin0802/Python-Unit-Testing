import unittest
import main


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(main.add(10, 5), 15)
        self.assertEqual(main.add(-1, 1), 0)
        self.assertEqual(main.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(main.subtract(10, 5), 5)
        self.assertEqual(main.subtract(-1, 1), -2)
        self.assertEqual(main.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(main.multiply(10, 5), 50)
        self.assertEqual(main.multiply(-1, 1), -1)
        self.assertEqual(main.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(main.divide(10, 5), 2)
        self.assertEqual(main.divide(-1, 1), -1)
        self.assertEqual(main.divide(-1, -1), 1)
        self.assertEqual(main.divide(5, 2), 2.5)

        with self.assertRaises(ValueError):
            main.divide(10, 0)

    def test_palindrome(self):
        self.assertTrue(main.palindrome('hello', 'olleh'))
        self.assertTrue(main.palindrome('python', 'nohtyp'))

    def test_even(self):
        self.assertTrue(main.evennum(2))
        self.assertTrue(main.evennum(4))
if __name__ == '__main__':
    unittest.main()
