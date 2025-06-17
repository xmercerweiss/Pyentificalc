from decimal import Decimal
import math as m

from .constants import Sign


class NumericalOperand:
    """An immutable number represented interally using base 10 scientific notation.

    Within this class, "magnitude" refers to the power to which 10 must be raised
    in order to produce the operand's value. eg: 144's magnitude is 2, as 144 = 1.44e2.
    """

    def __init__(self, coefficient: int, magnitude: int, sign: Sign = Sign.POS):
        """ Initializes an operand for representation with scientific notation.

        Args:
            coefficient: An integer representing the operand's coefficient.
            magnitude: An integer representing the operand's magnitude.
            sign: A Sign enum representing the operand's sign; defaults to positive.
        """
        self._coefficient = coefficient
        self._final_magnitude = magnitude
        self._sign = sign

    def to_decimal_value(self) -> Decimal:
        """Returns the closest decimal approximation of the operand's value.

        Returns: The operand's value as a Decimal object.
        """
        # A coeff of 0 always represents a value of 0
        if self._coefficient == 0:
            return Decimal(0)
        # How many decimal points are represented by coeff?
        # eg: a coeff of 123123 represents 1.23123
        # coeff_mag(123123) = 5, as .23123 has 5 digits
        coeff_magnitude = len(str(self._coefficient)) - 1
        # How many spaces do we need to move coeff's decimal point?
        # eg: if coeff = 123123 and the final magnitude = 2, our value is 123.123
        # to get 123.123, the decimal point of 123123 needs to be moved left 3 spaces
        # coeff_magnitude(123123) = 5, final_magnitude = 2, 2 - 5 = -3
        change_in_magnitude = Decimal(self._final_magnitude - coeff_magnitude)
        sign_factor = -1 if self._sign == Sign.NEG else 1
        return Decimal(self._coefficient) * sign_factor * 10 ** change_in_magnitude
