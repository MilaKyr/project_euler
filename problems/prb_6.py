"""
Sum square difference

The sum of the squares of the first ten natural numbers is: 1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is: (1+2+...+10)^2 = 55^2= 3025
Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is: 3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers
and the square of the sum.
"""
import sys


if __name__ == "__main__":
    try:
        max_value = int(sys.argv[1])
        range_values = range(1, max_value+1)
        sum_of_squares = sum([value**2 for value in range_values])
        square_of_sum = sum(range_values)**2
        print(f"The difference between the sum of the squares of range: 1-{max_value} "
              f"natural numbers and the square of the sum is {abs(sum_of_squares - square_of_sum)}")
    except Exception as e:
        print(e)
