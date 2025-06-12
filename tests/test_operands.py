from decimal import Decimal
import pytest

from src.core import NumericalOperand


@pytest.mark.parametrize("coeff, power, expected", [
    (1, 0, 1),
    (2, 1, 20),
    (3, 2, 300),
    (4, 3, 4_000),
    (5, 4, 50_000),
    (6, 5, 600_000),
    (7, 6, 7_000_000),
    (8, 7, 80_000_000),
    (9, 8, 900_000_000),
    (0, 9, 0)
])
def test_num_operand_whole_to_dec_approx(coeff, power, expected):
    num_opr = NumericalOperand(coeff, power)
    assert num_opr.to_decimal_value() == expected

@pytest.mark.parametrize("coeff, power, expected", [
    (12, 0, Decimal("1.2")),
    (255, 0, Decimal("2.55")),
    (123123, 0, Decimal("1.23123")),
    (255, 1, Decimal("25.5")),
    (1726182, 1, Decimal("17.26182")),
    (3242, 2, Decimal("324.2")),
    (18226, 2, Decimal("182.26")),
    (123123, 2, Decimal("123.123")),
    (716281716162, 5, Decimal("716281.716162")),
])
def test_num_operand_nonwhole_to_dec_approx(coeff, power, expected):
    num_opr = NumericalOperand(coeff, power)
    assert num_opr.to_decimal_value() == expected


#TODO Write tests for operands with negative magnitude.
