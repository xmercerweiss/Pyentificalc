from decimal import Decimal
import pytest

from pyentificalc.calculations import NumericalOperand, Sign


GET_POS_COEFF_NUM_OPR_INIT_ARGS = (
    (1, 0, Sign.POS, Decimal("1.0")),
    (55, 4, Sign.POS, Decimal("5.5")),
    (282, 1, Sign.POS, Decimal("2.82")),
    (88888, 8, Sign.POS, Decimal("8.8888")),
    (23, -4, Sign.POS, Decimal("2.3")),
    (99999, -10, Sign.POS, Decimal("9.9999")),
    (12345678, 2, Sign.POS, Decimal("1.2345678")),
    (90700, 0, Sign.POS, Decimal("9.07")),
    (100, 5, Sign.POS, Decimal("1.0")),
    (20300, 10, Sign.POS, Decimal("2.03"))
)

GET_NEG_COEFF_NUM_OPR_INIT_ARGS = (
    (1, 0, Sign.NEG, Decimal("-1.0")),
    (55, 4, Sign.NEG, Decimal("-5.5")),
    (282, 1, Sign.NEG, Decimal("-2.82")),
    (88888, 8, Sign.NEG, Decimal("-8.8888")),
    (23, -4, Sign.NEG, Decimal("-2.3")),
    (99999, -10, Sign.NEG, Decimal("-9.9999")),
    (12345678, 2, Sign.NEG, Decimal("-1.2345678")),
    (90700, 0, Sign.NEG, Decimal("-9.07")),
    (100, 5, Sign.NEG, Decimal("-1.0")),
    (20300, 10, Sign.NEG, Decimal("-2.03"))
)

GET_MAG_NUM_OPR_INIT_ARGS = (
    (1, 0, Sign.POS, 0),
    (55, 4, Sign.POS, 4),
    (282, 1, Sign.POS, 1),
    (88888, 8, Sign.POS, 8),
    (23, -4, Sign.POS, -4),
    (99999, -10, Sign.POS, -10),
    (12345678, 2, Sign.POS, 2),
    (90700, 0, Sign.POS, 0),
    (100, 5, Sign.POS, 5),
    (20300, 10, Sign.POS, 10)
)

GET_SIGN_NUM_OPR_INIT_ARGS = (
    (1, 0, Sign.PLUS_OR_MINUS, Sign.PLUS_OR_MINUS),
    (55, 4, Sign.PLUS_OR_MINUS, Sign.PLUS_OR_MINUS),
    (282, 1, Sign.POS, Sign.POS),
    (88888, 8, Sign.POS, Sign.POS),
    (23, -4, Sign.POS, Sign.POS),
    (99999, -10, Sign.POS, Sign.POS),
    (12345678, 2, Sign.NEG, Sign.NEG),
    (90700, 0, Sign.NEG, Sign.NEG),
    (100, 5, Sign.NEG, Sign.NEG),
    (20300, 10, Sign.NEG, Sign.NEG)
)

# TODO Write getter tests 
