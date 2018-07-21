"""
Problem 29 - Distinct Powers
https://projecteuler.net/problem=29
"""
import math


def distinct_powers():
    s = set()
    for a in range(2, 101):
        for b in range (2, 101):
            n = int(math.pow(a, b))
            s.add(n)
    return len(s)


if __name__ == "__main__":
    answer = distinct_powers()
    print(answer)