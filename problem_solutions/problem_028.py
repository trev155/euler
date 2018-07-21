"""
Problem 28 - Number Spiral Diagonals
https://projecteuler.net/problem=28
"""


def number_spiral_diagonals():
    """
    The 4 numbers in the corners of a square of dimension n can be computed with the formula:
    4n^2 - 6n + 6
    """
    x = corner_sum(1001)
    return x


def corner_sum(dim):
    if dim == 1:
        return 1
    acc = 1
    i = 3
    while i <= dim:
        corners = (4*i*i) - (6*i) + 6
        acc += corners
        i += 2
    return acc


if __name__ == "__main__":
    answer = number_spiral_diagonals()
    print(answer)