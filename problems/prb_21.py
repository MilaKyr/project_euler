"""
Amicable numbers

Let d(n) be defined as the sum of proper divisors of n (
numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
 each of a and b are called amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.
"""
from typing import Set, List
import math


def find_proper_divisors(value: int) -> List[int]:
    divisors = [1]
    max_value_sqrt = int(math.sqrt(value))
    start, step = (2, 1) if value % 2 == 0 else (3, 2)
    for divisor in range(start, max_value_sqrt, step):
        if value % divisor == 0:
            divisors.extend([divisor, int(value / divisor)])
    return divisors


def get_all_numbers(upper_value: int) -> Set[int]:
    amicable_numbers = set()
    for value in range(1, upper_value):
        if value not in amicable_numbers:
            fist_divisors = find_proper_divisors(value)
            sum_of_divisors_number_1 = sum(fist_divisors)
            second_divisors = find_proper_divisors(sum_of_divisors_number_1)
            sum_of_divisors_number_2 = sum(second_divisors)
            if value == sum_of_divisors_number_2 and value != sum_of_divisors_number_1:
                amicable_numbers.update({value, sum_of_divisors_number_2})
    return amicable_numbers


if __name__ == "__main__":
    print("The sum of all the amicable numbers under 10000 "
          f"is {sum(get_all_numbers(upper_value=10000))}")

