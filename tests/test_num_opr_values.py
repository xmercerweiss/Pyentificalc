from decimal import Decimal
import itertools as itertl
import pytest

from pyentificalc.calculations import NumericalOperand, Sign


WHOLE_NUM_OPR_INIT_ARGS = (
    (1, 0, Sign.POS, 1),
    (2, 1, Sign.POS, 20),
    (3, 2, Sign.POS, 300),
    (4, 3, Sign.POS, 4_000),
    (5, 4, Sign.POS, 50_000),
    (6, 5, Sign.POS, 600_000),
    (7, 6, Sign.POS, 7_000_000),
    (8, 7, Sign.POS, 80_000_000),
    (9, 8, Sign.POS, 900_000_000),
    (0, 9, Sign.POS, 0)
)

NONWHOLE_NUM_OPR_INIT_ARGS = (
    (12, 0, Sign.POS, Decimal("1.2")),
    (255, 0, Sign.POS, Decimal("2.55")),
    (123123, 0, Sign.POS, Decimal("1.23123")),
    (255, 1, Sign.POS, Decimal("25.5")),
    (1726182, 1, Sign.POS, Decimal("17.26182")),
    (3242, 2, Sign.POS, Decimal("324.2")),
    (18226, 2, Sign.POS, Decimal("182.26")),
    (123123, 2, Sign.POS, Decimal("123.123")),
    (716281716162, 5, Sign.POS, Decimal("716281.716162")),
)

NEG_MAG_NUM_OPR_INIT_ARGS = (
    (111, -1, Sign.POS, Decimal("0.111")),
    (123123, -1, Sign.POS, Decimal("0.123123")),
    (999999999999999, -1, Sign.POS, Decimal("0.999999999999999")),
    (456, -2, Sign.POS, Decimal("0.0456")),
    (77, -3, Sign.POS, Decimal("0.0077")),
    (3, -4, Sign.POS, Decimal("0.0003")),
    (4, -5, Sign.POS, Decimal("0.00004")),
    (5555, -5, Sign.POS, Decimal("0.00005555")),
    (6, -6, Sign.POS, Decimal("0.000006")),
    (1234567, -6, Sign.POS, Decimal("0.000001234567")),
    (1, -7, Sign.POS, Decimal("0.0000001")),
    (9876543, -7, Sign.POS, Decimal("0.0000009876543")),
    (1, -8, Sign.POS, Decimal("0.00000001")),
    (33333, -8, Sign.POS, Decimal("0.000000033333")),
    (1, -9, Sign.POS, Decimal("0.000000001")),
    (7777767, -9, Sign.POS, Decimal("0.000000007777767")),
)

NEG_COEFF_NUM_OPR_INIT_ARGS = (
    (1, 0, Sign.NEG, -1),
    (2, 1, Sign.NEG, -20),
    (3, 2, Sign.NEG, -300),
    (4, 3, Sign.NEG, -4_000),
    (5, 4, Sign.NEG, -50_000),
    (6, 5, Sign.NEG, -600_000),
    (7, 6, Sign.NEG, -7_000_000),
    (8, 7, Sign.NEG, -80_000_000),
    (9, 8, Sign.NEG, -900_000_000),
    (0, 9, Sign.NEG, 0),
    (12, 0, Sign.NEG, Decimal("-1.2")),
    (255, 0, Sign.NEG, Decimal("-2.55")),
    (123123, 0, Sign.NEG, Decimal("-1.23123")),
    (255, 1, Sign.NEG, Decimal("-25.5")),
    (1726182, 1, Sign.NEG, Decimal("-17.26182")),
    (3242, 2, Sign.NEG, Decimal("-324.2")),
    (18226, 2, Sign.NEG, Decimal("-182.26")),
    (123123, 2, Sign.NEG, Decimal("-123.123")),
    (716281716162, 5, Sign.NEG, Decimal("-716281.716162")),
    (111, -1, Sign.NEG, Decimal("-0.111")),
    (123123, -1, Sign.NEG, Decimal("-0.123123")),
    (999999999999999, -1, Sign.NEG, Decimal("-0.999999999999999")),
    (456, -2, Sign.NEG, Decimal("-0.0456")),
    (77, -3, Sign.NEG, Decimal("-0.0077")),
    (3, -4, Sign.NEG, Decimal("-0.0003")),
    (4, -5, Sign.NEG, Decimal("-0.00004")),
    (5555, -5, Sign.NEG, Decimal("-0.00005555")),
    (6, -6, Sign.NEG, Decimal("-0.000006")),
    (1234567, -6, Sign.NEG, Decimal("-0.000001234567")),
    (1, -7, Sign.NEG, Decimal("-0.0000001")),
    (9876543, -7, Sign.NEG, Decimal("-0.0000009876543")),
    (1, -8, Sign.NEG, Decimal("-0.00000001")),
    (33333, -8, Sign.NEG, Decimal("-0.000000033333")),
    (1, -9, Sign.NEG, Decimal("-0.000000001")),
    (7777767, -9, Sign.NEG, Decimal("-0.000000007777767")),
)

EXT_ZEROS_NUM_OPR_INIT_ARGS = (
    (100, 5, Sign.POS, Decimal("100000")),
    (90700, 2, Sign.POS, Decimal("907")),
    (2020, -1, Sign.POS, Decimal("0.202")),
    (90000000000, 2, Sign.POS, Decimal("900")),
    (1010102000, 3, Sign.POS, Decimal("1010.102")),
    (100, 0, Sign.NEG, Decimal("-1")),
    (220000, 3, Sign.NEG, Decimal("-2200")),
    (580, -10, Sign.NEG, Decimal("-0.00000000058")),
)

ALL_NUM_OPR_INIT_ARGS = tuple(itertl.chain(
    WHOLE_NUM_OPR_INIT_ARGS,
    NONWHOLE_NUM_OPR_INIT_ARGS,
    NEG_MAG_NUM_OPR_INIT_ARGS,
    NEG_COEFF_NUM_OPR_INIT_ARGS,
    EXT_ZEROS_NUM_OPR_INIT_ARGS
))

@pytest.mark.parametrize("coeff, mag, sign, expected", ALL_NUM_OPR_INIT_ARGS)
def test_num_oprand_value_is_decimal_obj(coeff, mag, sign, expected):
    num_opr = NumericalOperand(coeff, mag, sign)
    actual_value = num_opr.get_value()
    assert isinstance(actual_value, Decimal)

@pytest.mark.parametrize("coeff, mag, sign, expected", WHOLE_NUM_OPR_INIT_ARGS)
def test_num_operand_whole_to_dec_approx(coeff, mag, sign, expected):
    num_opr = NumericalOperand(coeff, mag, sign)
    actual_value = num_opr.get_value()
    assert actual_value == expected

@pytest.mark.parametrize("coeff, mag, sign, expected", NONWHOLE_NUM_OPR_INIT_ARGS)
def test_num_operand_nonwhole_to_dec_approx(coeff, mag, sign, expected):
    num_opr = NumericalOperand(coeff, mag, sign)
    actual_value = num_opr.get_value()
    assert actual_value == expected

@pytest.mark.parametrize("coeff, mag, sign, expected", NEG_MAG_NUM_OPR_INIT_ARGS)
def test_num_operand_neg_mag_to_dec_approx(coeff, mag, sign, expected):
    num_opr = NumericalOperand(coeff, mag, sign)
    actual_value = num_opr.get_value()
    assert actual_value == expected

@pytest.mark.parametrize("coeff, mag, sign, expected", NEG_COEFF_NUM_OPR_INIT_ARGS)
def test_num_operand_neg_whole_to_dec_approx(coeff, mag, sign, expected):
    num_opr = NumericalOperand(coeff, mag, sign)
    actual_value = num_opr.get_value()
    assert actual_value == expected

@pytest.mark.parametrize("coeff, mag, sign, expected", EXT_ZEROS_NUM_OPR_INIT_ARGS)
def test_num_operand_extra_zeros_to_dec_approx(coeff, mag, sign, expected):
    num_opr = NumericalOperand(coeff, mag, sign)
    actual_value = num_opr.get_value()
    assert actual_value == expected

# TODO Write plus or minus tests, change code to return tuple of values
