from random import randint
from custom_funcs import custom_max


def random_array(length, low, high):
    result = []
    for i in range(length):
        result.append(randint(low, high))
    return result


def test_custom_max_stress():
    for i in range(500):
        array = random_array(10000, -10000, 10000)
        assert custom_max(array) == max(array)
