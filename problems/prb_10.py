"""
Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
from prb_3 import all_prime_numbers

if __name__ == "__main__":
    prime_numbers = all_prime_numbers(2_000_000, use_sqrt=False)
    print(f"The sum of all the primes below two million is {sum(prime_numbers)}")