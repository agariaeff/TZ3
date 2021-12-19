from random import randint
from math import prod

from custom_funcs import custom_max, custom_min, custom_sum, custom_mul


def random_array(length, low, high):
    result = []
    for i in range(length):
        result.append(randint(low, high))
    return result


def test_custom_max():
    array = random_array(1000, -100, 100)
    assert custom_max(array) == max(array)


def test_custom_min():
    array = random_array(1000, -100, 100)
    assert custom_min(array) == min(array)


def test_custom_sum():
    array = random_array(1000, -100, 100)
    assert custom_sum(array) == sum(array)


def test_custom_mul():
    array = random_array(1000, -100, 100)
    assert custom_mul(array) == prod(array)
