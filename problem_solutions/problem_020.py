"""
Problem 20 - Factorial Digit Sum
https://projecteuler.net/problem=20
"""


def factorial_digit_sum():
    """
    Python will suprisingly be able to handle really large numbers, so long as you are able to generate them.
    """
    x = factorial(100)
    digit_sum = 0
    for c in str(x):
        digit_sum += int(c)
    return digit_sum


def factorial(n, acc=1):
    """
    Computing this with pure recursion will result in stack overflow for large n, so we
    make this function iterative.
    """
    while n > 1:
        n, acc = (n-1, acc*n)
    return acc


if __name__ == "__main__":
    answer = factorial_digit_sum()
    print(answer)
