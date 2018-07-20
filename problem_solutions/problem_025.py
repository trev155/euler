"""
Problem 25 - 1000 Digit Fibonnaci Number
https://projecteuler.net/problem=25
"""


def thousand_digit_fibonacci():
    """
    Idea is to write a fibonacci function iteratively so we don't get a stack overflow.
    In order to find the first fibonacci term that has 1000 digits, I just test different values until I find it.
    """
    n = 4782
    x = fib(n)
    print(x)
    print(len(str(x)))
    return n


def fib(n):
    if n <= 2:
        return 1
    prev = 1
    prev_two = 0
    i = 2
    while i < n:
        temp = prev_two
        prev_two = prev
        prev = temp + prev
        i += 1
    return prev + prev_two


if __name__ == "__main__":
    fib_terms = {}
    answer = thousand_digit_fibonacci()
    print(answer)
