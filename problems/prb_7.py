"""
10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""
from prb_3 import all_prime_numbers


if __name__ == "__main__":
    numbers = all_prime_numbers(10**12)
    print(f"The 10 001st prime number is {sorted(numbers)[10_000]}")
