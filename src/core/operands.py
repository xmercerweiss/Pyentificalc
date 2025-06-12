from decimal import Decimal
import math as m


class NumericalOperand:
    """An immutable number represented interally using base 10 scientific notation.

    Within this class, "magnitude" refers to the power to which 10 must be raised
    in order to produce the operand's value. eg: 144's magnitude is 2, as 144 = 1.44e2.
    """

    def __init__(self, coefficient: int, magnitude: int):
        """ Initializes an operand for representation with scientific notation.

        Args:
            coefficient: An integer representing the operand's coefficient.
            magnitude: An integer representing the operand's magnitude.
        """
        self._coeff = coefficient
        self._mag = magnitude

    def to_decimal_value(self) -> Decimal:
        """Returns the closest decimal approximation of the operand's value.

        Returns: The operand's value as a Decimal object.
        """
        if self._coeff == 0:
            return 0
        # eg: coeff_pow(46212) = 4, as the mantissa has 4 digits
        coeff_pow = m.floor(m.log10(self._coeff))
        # to reach desired mag, we must raise 10 to mag - coeff_pow
        # if coeff = 123123, mag = 2, then 123123 must be lowered by 3.
        # coeff_pow(123123) = 5; mag - 5 = -3; 123123*10^-3 = 123.123
        final_power = Decimal(self._mag - coeff_pow)
        return Decimal(self._coeff) * 10 ** final_power
