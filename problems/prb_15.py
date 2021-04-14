"""
Lattice paths

Starting in the top left corner of a 2×2 grid,
and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""
import sys
import math


def binomial_coefficient(n: int, k: int):
    return math.prod([(n+1-i)/i for i in range(1, k+1)])


if __name__ == "__main__":
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        # get Lattice paths by binomial_coefficient by (a+b, a)
        value = binomial_coefficient(a+b, b)
        print(f"In a grid {a}x{b} there are {value} routes")
    except Exception as e:
        print(e)
