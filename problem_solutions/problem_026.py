"""
Problem 26 - Reciprocal Cycles
https://projecteuler.net/problem=26
"""


def reciprocal_cycles():
    best_denominator = -1
    best_denominator_length = -1
    for i in range(2, 1000):
        val = 1.0 / i
        cycle = longest_cycle(str(val)[2:])
        if cycle > best_denominator_length:
            best_denominator = i
            best_denominator_length = cycle

    return best_denominator


def longest_cycle(s):
    """
    Given a string, find the length of the longest repeating substring.
    eg) In "abbcabbcabbc", return 4
    eg) In "abcdef", return 1
    """
    print(s)
    return -1


if __name__ == "__main__":
    answer = reciprocal_cycles()
    print(answer)
