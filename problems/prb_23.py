"""
Non-abundant sums

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and
it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written
as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known that
the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
from typing import List, Set
import math
from itertools import product


MAX_INTEGER = 28123


def is_abundant_number(number: int) -> bool:
    return True if sum(get_divisors(number)) > number else False


def get_divisors(number: int) -> List[int]:
    divisors = [1]
    upper_limit = int(math.sqrt(number))+1
    for divisor in range(2, upper_limit):
        if number % divisor == 0:
            divisors.extend([divisor, int(number/divisor)])
    return list(set(divisors))


def get_abundant_sums(numbers: List[int]) -> Set[int]:
    abundant_numbers = {number for number in numbers
                        if is_abundant_number(number)}
    return set(map(sum, product(abundant_numbers, repeat=2)))


if __name__ == "__main__":
    all_numbers = [num for num in range(1, MAX_INTEGER+1)]
    abundant_sums = get_abundant_sums(all_numbers)
    print(f"The sum of all the positive integers which "
          f"cannot be written as the sum of two "
          f"abundant numbers is {sum({num for num in all_numbers if num not in abundant_sums})}")
