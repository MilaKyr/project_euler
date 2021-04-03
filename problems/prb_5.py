"""
Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from functools import reduce

MIN_VALUE = 1
MAX_VALUE = 20
DENOMINATORS = [3, 4, 6, 7, 8, 9, 11, 13, 16, 17, 19]  # avoid 5 and 10, they are checked separately


def get_last_digit(value: int) -> int:
    return int(list(str(value))[-1])


def increment(value: int) -> int:
    last_digit = get_last_digit(value)
    if last_digit == 0:
        return value + 10
    elif last_digit % 2 == 0:
        return value + 2
    return value + 1


def is_dividable(value: int) -> bool:
    if get_last_digit(value) == 0:
        for denominator in DENOMINATORS:
            if value % denominator != 0:
                return False
        return True
    return False


def get_min_product() -> int:
    product = MAX_VALUE
    max_product = reduce(lambda x, y: x * y, range(MIN_VALUE, MAX_VALUE + 1))
    while product < max_product:
        dividable = is_dividable(product)
        if dividable:
            return product
        product = increment(product)
    return max_product


if __name__ == "__main__":
    try:
        min_product = get_min_product()
        print("The smallest positive number that is evenly divisible by all "
              f"of the numbers from {MIN_VALUE} to {MAX_VALUE} is {min_product}")
    except Exception as e:
        print(e)

