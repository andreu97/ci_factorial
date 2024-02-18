import pytest
from src.tdd import factorial


def test_tdd():
    assert factorial(1) == 1


def test_calc_error():
    with pytest.raises(ValueError):
        factorial(-1)


def test_factorial_cinc():
    assert factorial(5) == 120


def test_typerror():
    with pytest.raises(TypeError):
        factorial("a")
