"""Module to test Fraction"""
import unittest
from Fraction.fraction import Fraction


class FactTestCase(unittest.TestCase):
    """Class to test the class Fraction"""
    def test_den_is_zero_error(self):
        """Test if ZeroDivisionError is raised"""
        with self.assertRaises(ZeroDivisionError) as zero_error1:
            Fraction(1, 0)
        self.assertEqual(zero_error1.exception.args[0], "The denominator of a fraction can't be 0")
        with self.assertRaises(ZeroDivisionError) as zero_error2:
            Fraction(12, 0)
        self.assertEqual(zero_error2.exception.args[0], "The denominator of a fraction can't be 0")
        with self.assertRaises(ZeroDivisionError) as zero_error3:
            Fraction(120, 0)
        self.assertEqual(zero_error3.exception.args[0], "The denominator of a fraction can't be 0")

    def test_type_error(self):
        """Test if TypeError is raised"""
        with self.assertRaises(TypeError) as type_error1:
            print(Fraction(2, 4) ** 'random')
        self.assertEqual(type_error1.exception.args[0], 'Must be type int')
        with self.assertRaises(TypeError) as type_error2:
            print(Fraction(4, 4) ** Fraction(1, 2))
        self.assertEqual(type_error2.exception.args[0], 'Must be type int')
        with self.assertRaises(TypeError) as type_error3:
            print(Fraction(8, 4) ** [1])
        self.assertEqual(type_error3.exception.args[0], 'Must be type int')


if __name__ == '__main__':
    unittest.main()
