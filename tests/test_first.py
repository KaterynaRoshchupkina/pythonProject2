import pytest
from src import my_function


@pytest.mark.parametrize('a, b, c', [(1, 2, 3), (5, 3, 8), (20, 40, 60)])
def test_add(a, b, c):
    assert my_function.add(a, b) == c
