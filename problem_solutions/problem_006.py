"""
Problem 6 - Sum Square Difference
https://projecteuler.net/problem=6
"""


def sum_square_difference():
    """
    Given a list of N numbers [a, b, c] the difference between
    a^2 + b^2 + c^2
    and
    (a + b + c)^2
    can be written as:
    2ab + 2ac + 2bc

    This can be seen through mathematical expansion of the second expression.
    Following this pattern, we can compute such a difference for a list of any number of numbers.

    The code below carries out this process, albeit in a roundabout, but efficient manner.
    """
    lst = list(range(1, 101))
    acc = 0
    for e in lst:
        for f in lst:
            if e != f:
                acc = acc + (e * f)
    return acc


if __name__ == "__main__":
    answer = sum_square_difference()
    print(answer)
