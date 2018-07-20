"""
Problem 21 - Amicable Numbers
https://projecteuler.net/problem=21
"""
import math


def amicable_numbers():
    # compute the proper divisors and sums for each number
    seen = {}
    for i in range(1, 10000):
        proper_divs = proper_divisors(i)
        proper_divs_sum = sum(proper_divs)
        seen[i] = proper_divs_sum

    # iterate over the mappings to find amicable numbers
    total = 0
    processed = set()
    for (k, v) in seen.items():
        if k == v:
            # by definition of amicable numbers
            continue
        if k in processed:
            # don't count this k,v pair twice
            continue
        if v in seen and seen[v] == k:
            total += k
            total += v
            processed.add(v)
            print(k, v)

    return total


def proper_divisors(n):
    divisors = set()
    for i in range(1, int(math.ceil(math.sqrt(n))) + 1):
        if n % i == 0 and n != i:
            divisors.add(i)
            if i != 1:
                divisors.add(n // i)
    return divisors


if __name__ == "__main__":
    answer = amicable_numbers()
    print(answer)
