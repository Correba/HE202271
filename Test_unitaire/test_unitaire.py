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
        with self.assertRaises(TypeError) as type_error3:
            print(Fraction(8, 4) / 'something')
        self.assertEqual(type_error3.exception.args[0], 'Must be an int or a Fraction')

    def test_declaration(self):
        """Test declaration of a Fraction"""
        fraction1 = Fraction(1, 2)
        self.assertEqual(fraction1.numerator, 1)
        self.assertEqual(fraction1.denominator, 2)
        fraction2 = Fraction(-3, 4)
        self.assertEqual(fraction2.numerator, -3)
        self.assertEqual(fraction2.denominator, 4)
        fraction3 = Fraction(8, -4)
        self.assertEqual(fraction3.numerator, -2)
        self.assertEqual(fraction3.denominator, 1)
        fraction4 = Fraction(2, 2)
        self.assertEqual(fraction4.numerator, 1)
        self.assertEqual(fraction4.denominator, 1)
        fraction5 = Fraction(13, 4)
        self.assertEqual(fraction5.numerator, 13)
        self.assertEqual(fraction5.denominator, 4)

    def test_str(self):
        """Test textual representation of a Fraction"""
        self.assertEqual(str(Fraction(1, 2)), "1/2")
        self.assertEqual(str(Fraction(3, 4)), "3/4")
        self.assertEqual(str(Fraction(8, 4)), "2/1")
        self.assertEqual(str(Fraction(2, 2)), "1/1")
        self.assertEqual(str(Fraction(13, 4)), "13/4")

    def test_mixed_number(self):
        """Test mixed number representation of a Fraction"""
        self.assertEqual(Fraction(1, 2).as_mixed_number(), "0 + 1/2")
        self.assertEqual(Fraction(3, 4).as_mixed_number(), "0 + 3/4")
        self.assertEqual(Fraction(8, 4).as_mixed_number(), "2 + 0/1")
        self.assertEqual(Fraction(2, 2).as_mixed_number(), "1 + 0/1")
        self.assertEqual(Fraction(13, 4).as_mixed_number(), "3 + 1/4")

    def test_add(self):
        """Test add operation on Fraction"""
        self.assertEqual(str(Fraction(1, 2) + Fraction(3, 4)), "5/4")
        self.assertEqual(str(Fraction(8, 4) + Fraction(2, 2)), "3/1")
        self.assertEqual(str(Fraction(3, 4) + Fraction(13, 4)), "4/1")
        self.assertEqual(str(Fraction(1, 2) + 2), "5/2")
        self.assertEqual(str(Fraction(-1, 2) + 2), "3/2")

    def test_sub(self):
        """Test sub operation on Fraction"""
        self.assertEqual(str(Fraction(1, 2) - Fraction(3, 4)), "-1/4")
        self.assertEqual(str(Fraction(8, 4) - Fraction(2, 2)), "1/1")
        self.assertEqual(str(Fraction(3, 4) - Fraction(13, 4)), "-5/2")
        self.assertEqual(str(Fraction(1, 2) - 2), "-3/2")
        self.assertEqual(str(Fraction(-1, 2) - 2), "-5/2")

    def test_mul(self):
        """Test mul operation on Fraction"""
        self.assertEqual(str(Fraction(1, 2) * Fraction(3, 4)), "3/8")
        self.assertEqual(str(Fraction(8, 4) * Fraction(2, 2)), "2/1")
        self.assertEqual(str(Fraction(3, 4) * Fraction(13, 4)), "39/16")
        self.assertEqual(str(Fraction(1, 2) * 2), "1/1")
        self.assertEqual(str(Fraction(-1, 2) * 2), "-1/1")

    def test_div(self):
        """Test div operation on Fraction"""
        self.assertEqual(str(Fraction(1, 2) / Fraction(3, 4)), "2/3")
        self.assertEqual(str(Fraction(8, 4) / Fraction(2, 2)), "2/1")
        self.assertEqual(str(Fraction(3, 4) / Fraction(13, 4)), "3/13")
        self.assertEqual(str(Fraction(1, 2) / 2), "1/4")
        self.assertEqual(str(Fraction(-1, 2) / 2), "-1/4")

    def test_pow(self):
        """Test pow operation on Fraction"""
        self.assertEqual(str(Fraction(1, 2) ** 1), "1/2")
        self.assertEqual(str(Fraction(8, 4) ** 4), "16/1")
        self.assertEqual(str(Fraction(3, 4) ** 2), "9/16")

    def test_eq(self):
        """Test == operation on Fraction"""
        self.assertTrue(Fraction(1, 2) == Fraction(2, 4))
        self.assertFalse(Fraction(1, 2) == Fraction(3, 4))
        self.assertTrue(Fraction(2, 1) == 2)
        self.assertFalse(Fraction(3, 4) == 4)

    def test_float(self):
        """Test conversion of Fraction to float"""
        self.assertEqual(float(Fraction(1, 2)), 0.5)
        self.assertEqual(float(Fraction(1, 1)), 1.0)
        self.assertEqual(float(Fraction(3, 2)), 1.5)
        self.assertEqual(float(Fraction(-3, 4)), -0.75)

    def test_abs(self):
        """Test abs of a Fraction"""
        self.assertEqual(abs(Fraction(1, 2)), Fraction(1, 2))
        self.assertEqual(abs(Fraction(-1, 2)), Fraction(1, 2))
        self.assertEqual(abs(Fraction(3, -2)), Fraction(3, 2))
        self.assertEqual(abs(Fraction(-16, 2)), Fraction(8, 1))

    def test_gt(self):
        """Test > comparison on Fraction"""
        self.assertGreater(Fraction(1, 2), Fraction(1, 4))
        self.assertGreater(2, Fraction(1, 8))
        self.assertGreater(-1, Fraction(-2, 1))
        self.assertGreater(Fraction(1, 2), 0)

    def test_ge(self):
        """Test >= comparison on Fraction"""
        self.assertGreaterEqual(Fraction(1, 2), 0.5)
        self.assertGreaterEqual(2, Fraction(1, 8))
        self.assertGreaterEqual(0, Fraction(-1, 2))
        self.assertGreaterEqual(0.5, Fraction(0))

    def test_lt(self):
        """Test < comparison on Fraction"""
        self.assertLess(Fraction(1, 4), Fraction(1, 2))
        self.assertLess(Fraction(1, 8), 2)
        self.assertLess(Fraction(-2, 1), -1)
        self.assertLess(0, Fraction(1, 2))

    def test_le(self):
        """Test <= comparison on Fraction"""
        self.assertLessEqual(0.5, Fraction(1, 2))
        self.assertLessEqual(Fraction(1, 8), 2)
        self.assertLessEqual(Fraction(-1, 2), 0)
        self.assertLessEqual(Fraction(0), 0.5)

    def test_zero(self):
        """Test if Fraction == 0"""
        self.assertTrue(Fraction(0, 15).is_zero())
        self.assertTrue(Fraction(0).is_zero())
        self.assertFalse(Fraction(1, 2).is_zero())
        self.assertFalse(Fraction(12).is_zero())

    def test_int(self):
        """Test if Fraction value is an int"""
        self.assertTrue(Fraction(2).is_integer())
        self.assertTrue(Fraction(8, 4).is_integer())
        self.assertFalse(Fraction(2, 3).is_integer())
        self.assertFalse(Fraction(16, 15).is_integer())

    def test_proper(self):
        """Test if absolute value of Fraction is < 1"""
        self.assertTrue(Fraction(1, 2).is_proper())
        self.assertTrue(Fraction(-15, 16).is_proper())
        self.assertFalse(Fraction(3, 2).is_proper())
        self.assertFalse(Fraction(-1).is_proper())

    def test_unit(self):
        """Test if Fraction numerator == 1"""
        self.assertTrue(Fraction(1, 8).is_unit())
        self.assertTrue(Fraction(2, 4).is_unit())
        self.assertFalse(Fraction(5, 2).is_unit())
        self.assertFalse(Fraction(2, 3).is_unit())

    def test_adjacent(self):
        """Test if the difference between two Fraction is a unit"""
        self.assertTrue(Fraction(1, 8).is_adjacent_to(Fraction(1, 4)))
        self.assertTrue(Fraction(2, 4).is_adjacent_to(Fraction(0)))
        self.assertFalse(Fraction(4, 3).is_adjacent_to(2))
        self.assertFalse(Fraction(2, 3).is_adjacent_to(Fraction(2, 3)))


if __name__ == '__main__':
    unittest.main()
