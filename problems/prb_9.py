"""
Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
from typing import Tuple, Optional
import math
import functools

MAX_A = 500
MAX_B = 500
TRIPLET_SUM = 1000


def get_pythagorean_triplet() -> Optional[Tuple[int, int, float]]:
    for a in range(3, MAX_A):
        for b in range(a + 1, MAX_B):
            c = a ** 2 + b ** 2
            sqrt_c = math.sqrt(c)
            if int(sqrt_c + 0.5) ** 2 == c:
                triplet = (a, b, sqrt_c)
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
