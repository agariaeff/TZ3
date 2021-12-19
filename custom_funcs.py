def custom_sum(numbers):
    result = 0
    for num in numbers:
        result += num
    return result


def custom_mul(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


def custom_max(numbers):
    temp = numbers[0]
    for num in numbers:
        if num > temp:
            temp = num
    return temp


def custom_min(numbers):
    temp = numbers[0]
    for num in numbers:
        if num < temp:
            temp = num
    return temp
