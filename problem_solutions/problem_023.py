"""
Problem 23 - Non-Abundant Sums
https://projecteuler.net/problem=23
"""
import math


def non_abundant_sums():
    # based on proper divisors, classify all the numbers from 1 to 28123
    # note that we only need to keep track of abundants, but I store them all anyways
    perfects = []
    deficients = []
    abundants = []
    for i in range(1, 28123):
        proper_divs = proper_divisors(i)
        proper_divs_sum = sum(proper_divs)
        if proper_divs_sum == i:
            # perfect number
            perfects.append(i)
        elif proper_divs_sum < i:
            # deficient number
            deficients.append(i)
        else:
            # abundant number
            abundants.append(i)

    # find all numbers that cannot be written as the sum of 2 abundant numbers
    # it is already known / given that all numbers > 28123 can be written as the sum of 2 abundant numbers
    # and it is known that 24 is the smallest such number
    non_abundants = []
    candidates = []
    candidates_index = 0
    for i in range(24, 28123):
        print(i)

        # can i be written as the sum of 2 abundant numbers?
        for c in range(candidates_index, len(abundants)):
            elem = abundants[c]
            if elem >= i:
                break
            candidates.append(elem)
            candidates_index = c + 1

        if not list_sum(candidates, i):
            non_abundants.append(i)

    ans = sum(non_abundants)
    return ans


def list_sum(lst, target):
    """
    Given a list of numbers, is it possible to take 2 of them to sum to the target?
    The list contains only numbers < target.
    """
    print("start", target)
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            a = lst[i]
            b = lst[j]
            if a + b == target:
                return True
    return False


def binary_search_sum(lst, target):
    """
    Binary search implementation
    """
    left = 0
    right = len(lst) - 1
    while left < right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return 1


def proper_divisors(n):
    divisors = set()
    for i in range(1, int(math.ceil(math.sqrt(n))) + 1):
        if n % i == 0 and n != i:
            divisors.add(i)
            if i != 1:
                divisors.add(n // i)
    return divisors


if __name__ == "__main__":
    answer = non_abundant_sums()
    print(answer)