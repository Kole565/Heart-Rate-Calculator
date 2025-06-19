import os
import sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "../..")
sys.path.append(PROJECT_ROOT)

import pytest

from backend.calculator import Calculator
from backend.exceptions import *


def test_empty_init():
    Calculator()

def test_results_update():
    age = 20
    rest_hr = 60

    calculator = Calculator()

    calculator.calculate(age, rest_hr)
    first = calculator.zones[:]

    calculator.calculate(age + 1, rest_hr + 1)
    second = calculator.zones[:]

    assert (first != second) and (not (first is second))

def test_zones_init():
    age = 20
    rest_hr = 60

    calculator = Calculator(age, rest_hr)

    assert calculator.zones == [
        [126.5, 153.1],
        [153.1, 166.4],
        [166.4, 175.71],
        [175.71, 185.02],
        [185.02, 193],
    ]

def test_calc_init_vs_runtime():
    age = 20
    rest_hr = 60

    calculator = Calculator(age, rest_hr)

    first = calculator.zones[:]

    calculator.calculate(age, rest_hr)

    second = calculator.zones[:]

    assert (first == second) and (not (first is second))

@pytest.mark.parametrize(
    "age, rest_hr", [
        (10, 60), (150, 60), (20, 0), (20, 150)
    ]
)
def test_invalid_input(age, rest_hr):
    with pytest.raises(InvalidInput):
        Calculator(age, rest_hr)

def test_float_values():
    age = 20
    rest_hr = 60.0

    calculator = Calculator(age, rest_hr)
    calculator.calculate(age, rest_hr)
