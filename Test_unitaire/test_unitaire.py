"""Module to test Fraction"""
import unittest
from Fraction.fraction import Fraction


class FactTestCase(unittest.TestCase):
    """Class to test the class Fraction"""
    def test_den_is_zero(self):
        """Test if ZeroDivisionError is raised"""
        with self.assertRaises(ZeroDivisionError) as error:
            Fraction(1, 0)


if __name__ == '__main__':
    unittest.main()
