"""
Problem 5 - Smallest Multiple
https://projecteuler.net/problem=5
"""


def smallest_multiple():
    """
    This doesn't have great runtime, but it's at least more reasonable.
    The LCM algorithm is basically: a*b / gcd(a,b).
    gcd(a,b) should be iterative, not recursive, or else you'll get stack overflow.
    """
    num = 20
    for i in range(20, 1, -1):
        num = least_common_multiple(num, i)
    return num


def least_common_multiple(a, b):
    return (a * b) / gcd(a, b)


def gcd(a, b):
    while True:
        if a == b:
            # base case
            return a
        elif a > b:
            a = a - b
        else:
            b = b - a


if __name__ == "__main__":
    answer = smallest_multiple()
    print(answer)
