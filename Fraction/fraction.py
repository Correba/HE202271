"""Module to use math operations"""
import math


class Fraction:
    """Class representing a fraction and operations on it

    Author : M. Verbiest
    Date : November 2023
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        :pre:
        - num : an int that represents the numerator of a fraction
        - den : an int that represents the denominator of a fraction
        :post:
        - numerator : the reduced numerator of a fraction
        - denominator : the positive reduced denominator of a fraction
        :raises: ZeroDivisionError if den value is 0
        """
        if den == 0:
            raise ZeroDivisionError("The denominator of a fraction can't be 0")

        abs_num = abs(num)
        if num / den < 0:
            num = -abs_num
        else:
            num = abs_num

        common_divisor = math.gcd(num, den)
        self.__numerator = num // common_divisor
        self.__denominator = abs(den) // common_divisor

    @property
    def numerator(self):
        """This gets the value of numerator
        :post: returns the value of numerator
        """
        return self.__numerator

    @property
    def denominator(self):
        """This gets the value of denominator
        :post: returns the value of denominator
        """
        return self.__denominator

    @staticmethod
    def is_fraction(num: int):
        """A function to set a value to Fraction

        :pre: a numerical value
        :post: returns a fraction of the value
        :raises: ValueError if num is not an int or a Fraction
        """

        if isinstance(num, int):
            num = Fraction(num)
        if not isinstance(num, Fraction):
            raise ValueError('Must be an int or a fraction')
        return num

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction
        
        :post: Returns the value of the numerator and the denominator separated by /
        """
        return f'{self.__numerator}/{self.__denominator}'

    def __repr__(self) -> str:
        """Return the textual representation of the reduced form of the fraction

        :post: the numerator and the denominator separated by a backslash
        """
        return str(self)

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        :post: returns the int value of the fraction and rest of the fraction separated by +
        """
        int_value = self.numerator // self.denominator
        fraction_value = Fraction(self.numerator % self.denominator, self.denominator)
        return f'{int_value} + {fraction_value}'

    # ------------------ Operators overloading ------------------

    def __add__(self, other: int):
        """Overloading of the + operator for fractions

         :pre: a numerical value
         :post: returns the result of the addition of two elements
         :raises: ValueError if other not int
         """
        other = self.is_fraction(other)
        add_num = self.numerator * other.denominator + self.denominator * other.numerator
        add_den = self.denominator * other.denominator
        return Fraction(add_num, add_den)

    def __sub__(self, other: int):
        """Overloading of the - operator for fractions

        :pre: a numerical value
        :post: returns the result of the subtraction of two elements
        :raises: ValueError if other not int
        """
        other = self.is_fraction(other)
        sub_num = self.numerator * other.denominator - self.denominator * other.numerator
        sub_den = self.denominator * other.denominator
        return Fraction(sub_num, sub_den)

    def __mul__(self, other: int):
        """Overloading of the * operator for fractions

        :pre: a numerical value
        :post: returns the result of the multiplication of two elements
        :raises: ValueError if other not int
        """
        other = self.is_fraction(other)
        mul_num = self.numerator * other.numerator
        mul_den = self.denominator * other.denominator
        return Fraction(mul_num, mul_den)

    def __truediv__(self, other: int):
        """Overloading of the / operator for fractions

        :pre: a numerical value
        :post: returns the result of the division of two elements
        :raises: ValueError if other not int
        """
        other = self.is_fraction(other)
        div_num = self.numerator * other.denominator
        div_den = self.denominator * other.numerator
        return Fraction(div_num, div_den)

    def __pow__(self, other: int):
        """Overloading of the ** operator for fractions

        :pre: an integer
        :post: the value of the fraction to the power of an int
        :raises: if other is not an int raises a TypeError
        """
        if not isinstance(other, int):
            raise TypeError('Must be type int')

        pow_num = self.numerator ** other
        pow_den = self.denominator ** other
        return Fraction(pow_num, pow_den)

    def __eq__(self, other: int) -> bool:
        """Overloading of the == operator for fractions

        :pre: an int
        :post: returns the equality between two Fraction
        """
        other = self.is_fraction(other)
        return float(self) == float(other)

    def __float__(self) -> float:
        """Returns the decimal value of the fraction

        :post: the decimal value of the fraction
        """
        return self.numerator / self.denominator

    # TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)

    def __abs__(self):
        """Returns the absolute value of the fraction

        :post: returns the absolute value of Fraction
        """
        return Fraction(abs(self.numerator), self.denominator)

    def __gt__(self, other: int) -> bool:
        """Overloading of the > operator for fractions

        :pre: an integer or a Fraction
        :post: the current fraction is greater than the other fraction
        """
        return float(self) > float(other)

    def __ge__(self, other: int) -> bool:
        """Overloading of the >= operator for fractions

        :pre: an integer or a Fraction
        :post: the current fraction equals or is greater than the other fraction
        """
        return float(self) >= float(other)

    def __lt__(self, other: int) -> bool:
        """Overloading of the < operator for fractions

        :pre: an integer or a Fraction
        :post: the current fraction is lower than the other fraction
        """
        return float(self) < float(other)

    def __le__(self, other: int) -> bool:
        """Overloading of the <= operator for fractions

        :pre: an integer or a Fraction
        :post: the current fraction equals or is lower than the other fraction
        """
        return float(self) <= float(other)

    # ------------------ Properties checking  ------------------

    def is_zero(self) -> bool:
        """Check if a fraction's value is 0

        :post: returns True if Fraction value is 0 else returns False
        """
        return not self.numerator

    def is_integer(self) -> bool:
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        :post: returns True if Fraction value is an int else returns False
        """
        return self.denominator == 1

    def is_proper(self) -> bool:
        """Check if the absolute value of the fraction is < 1

        :post: returns True if Fraction value is < 1 else returns False
        """
        return abs(float(self)) < 1

    def is_unit(self) -> bool:
        """Check if a fraction's numerator is 1 in its reduced form

        :post: returns True if Fraction's numerator value is 1 else returns False
        """
        return self.numerator == 1

    def is_adjacent_to(self, other) -> bool:
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacent if the absolute value of the difference them is a unit fraction

        :pre: a Fraction
        :post: returns True if two Fraction are adjacent else returns False
        """
        return abs(self - other).is_unit()


def test_type(fraction, adjacent):
    """Test function for the types methods"""
    print(f'{fraction} :')
    print(f'---> Mixed number : {fraction.as_mixed_number()}')
    print(f'---> Is zero : {fraction.is_zero()}')
    print(f'---> Is int : {fraction.is_integer()}')
    print(f'---> Is proper : {fraction.is_proper()}')
    print(f'---> Is unit : {fraction.is_unit()}')
    print(f'---> Is adjacent : {fraction.is_adjacent_to(adjacent)}\n')


if __name__ == '__main__':
    try:
        fraction1 = Fraction(3, 0)
        print(fraction1)
    except ZeroDivisionError as error:
        print(f'Error : \n---> {error}\n')

    test_type(Fraction(10, 5), Fraction(9, 5))
    test_type(Fraction(1, 4), Fraction(3, 4))
