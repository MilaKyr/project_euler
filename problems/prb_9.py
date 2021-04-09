"""
Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
from typing import Tuple, Optional
import functools

MAX_A = 100
MAX_B = 100
TRIPLET_SUM = 1000


def get_pythagorean_triplet() -> Optional[Tuple[int, int, float]]:
    for n in range(1, MAX_A):
        for m in range(n+1, MAX_A):
            triplet = (2*m*n, m**2 - n**2, m**2 + n**2)  # Euclid's formula for natural numbers
            if sum(triplet) == TRIPLET_SUM:
                return triplet
    return None


if __name__ == "__main__":
    found_triplet = get_pythagorean_triplet()
    if found_triplet:
        product = functools.reduce(lambda x, y: x * y, get_pythagorean_triplet())
        print(f"The product abc is {product} for Pythagorean "
              f"triplet for which a + b + c = {TRIPLET_SUM}")
    else:
        print(f"No Pythagorean triplet found for which a + b + c = {TRIPLET_SUM}")
