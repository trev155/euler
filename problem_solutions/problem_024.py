"""
Problem 24 - Lexicographic Permutations
https://projecteuler.net/problem=24
"""


def lexicographic_permutations():
    from itertools import permutations
    l = list(permutations([0, 1, 3, 4, 5, 6, 7, 8, 9]))
    iters = 1000000 - 725760
    return [2] + list(l[iters - 1])


if __name__ == "__main__":
    answer = lexicographic_permutations()
    print(answer)
