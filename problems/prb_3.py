"""
Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
from typing import Set
import math
import sys
from copy import deepcopy


# Eratosthene’s method with capping to sqrt(value)
def all_prime_numbers(value: int) -> Set[int]:
    sqrt_max_value = int(math.sqrt(value))
    possible_values = {2, *set(range(3, sqrt_max_value, 2))}
    trespassed_values = set()
    for possible_value in sorted(possible_values):
        sub_passed = get_trespassed_for(possible_value, sqrt_max_value, possible_values)
        trespassed_values.update(sub_passed)
    return possible_values - trespassed_values


def get_trespassed_for(value, max_value, possible_values):
    sub_trespassed = set()
    new_value = deepcopy(value)
    while new_value < max_value:
        new_value += value
        if new_value in possible_values:
            sub_trespassed.add(new_value)
    return sub_trespassed


def max_prime_factor(for_value: int, from_set: Set[int]):
    for prime_number in sorted(from_set, reverse=True):
        if for_value % prime_number == 0:
            return prime_number


if __name__ == "__main__":
    try:
        num = int(sys.argv[1])
        prime_num = all_prime_numbers(num)
        max_prime_factor = max_prime_factor(for_value=num, from_set=prime_num)
        print(f"The largest prime factor of the number {num} is {max_prime_factor}")
    except Exception as e:
        print(e)
