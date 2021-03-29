import sys
"""
Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""


def multiples(num: int):
    return sum([v for v in range(1, num) if v % 5 == 0 or v % 3 == 0])


if __name__ == "__main__":
    try:
        num = int(sys.argv[1])
        print(f"The sum of all the multiples of 3 or 5 below {num} is {multiples(num)}")
    except Exception as e:
        print(e)


