"""
Largest palindrome product

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
import sys
from typing import List


def is_palindrome(value: int) -> bool:
    numbers = list(str(value))
    middle = int(len(numbers) / 2)
    first_part = numbers[:middle]
    second_part = numbers[middle:] if len(numbers) % 2 == 0 else numbers[middle+1:]
    return True if first_part == second_part[::-1] else False


def get_all_products(min_value: int, max_value: int) -> List[int]:
    products = []
    max_for_range = max_value + 1
    while max_value > min_value:
        for value in sorted(range(min_value, max_for_range), reverse=True):
            products.append(max_value * value)
        max_value -= 1
    return products


def find_biggest_palindrome(products: List[int]) -> int:
    for product in sorted(products, reverse=True):
        if is_palindrome(product):
            return product


if __name__ == "__main__":
    try:
        min_value = int(sys.argv[1])
        max_value = int(sys.argv[2])
        products = get_all_products(min_value, max_value)
        len_digits = len(str(max_value))
        print("The largest palindrome made from the "
              f"product of two {len_digits}-digit numbers is {find_biggest_palindrome(products)}")
    except Exception as e:
        print(e)