from decimal import Decimal
import itertools as itertl
import pytest

from pyentificalc.calculations import NumericalOperand


WHOLE_NUM_OPR_INIT_ARGS = (
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
)

NONWHOLE_NUM_OPR_INIT_ARGS = (
    (12, 0, Decimal("1.2")),
    (255, 0, Decimal("2.55")),
    (123123, 0, Decimal("1.23123")),
    (255, 1, Decimal("25.5")),
    (1726182, 1, Decimal("17.26182")),
    (3242, 2, Decimal("324.2")),
    (18226, 2, Decimal("182.26")),
    (123123, 2, Decimal("123.123")),
    (716281716162, 5, Decimal("716281.716162")),
)

NEG_MAG_NUM_OPR_INIT_ARGS = (
    (111, -1, Decimal("0.111")),
    (123123, -1, Decimal("0.123123")),
    (999999999999999, -1, Decimal("0.999999999999999")),
    (456, -2, Decimal("0.0456")),
    (77, -3, Decimal("0.0077")),
    (3, -4, Decimal("0.0003")),
    (4, -5, Decimal("0.00004")),
    (5555, -5, Decimal("0.00005555")),
    (6, -6, Decimal("0.000006")),
    (1234567, -6, Decimal("0.000001234567")),
    (1, -7, Decimal("0.0000001")),
    (9876543, -7, Decimal("0.0000009876543")),
    (1, -8, Decimal("0.00000001")),
    (33333, -8, Decimal("0.000000033333")),
    (1, -9, Decimal("0.000000001")),
    (7777767, -9, Decimal("0.000000007777767")),
)

ALL_NUM_OPR_INIT_ARGS = tuple(itertl.chain(
    WHOLE_NUM_OPR_INIT_ARGS,
    NONWHOLE_NUM_OPR_INIT_ARGS,
    NEG_MAG_NUM_OPR_INIT_ARGS,
))

@pytest.mark.parametrize("coeff, mag, expected", ALL_NUM_OPR_INIT_ARGS)
def test_num_oprand_value_is_decimal_obj(coeff, mag, expected):
    num_opr = NumericalOperand(coeff, mag)
    actual_value = num_opr.to_decimal_value()
    assert isinstance(actual_value, Decimal)

@pytest.mark.parametrize("coeff, mag, expected", WHOLE_NUM_OPR_INIT_ARGS)
def test_num_operand_whole_to_dec_approx(coeff, mag, expected):
    num_opr = NumericalOperand(coeff, mag)
    actual_value = num_opr.to_decimal_value()
    assert actual_value == expected

@pytest.mark.parametrize("coeff, mag, expected", NONWHOLE_NUM_OPR_INIT_ARGS)
def test_num_operand_nonwhole_to_dec_approx(coeff, mag, expected):
    num_opr = NumericalOperand(coeff, mag)
    actual_value = num_opr.to_decimal_value()
    assert actual_value == expected

@pytest.mark.parametrize("coeff, mag, expected", NEG_MAG_NUM_OPR_INIT_ARGS)
def test_num_operand_neg_mag_to_dec_approx(coeff, mag, expected):
    num_opr = NumericalOperand(coeff, mag)
    actual_value = num_opr.to_decimal_value()
    assert actual_value == expected
