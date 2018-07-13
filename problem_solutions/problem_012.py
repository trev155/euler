"""
Problem 12 - Highly Divisible Triangular Number
https://projecteuler.net/problem=12
"""
import math


def highly_divisble_triangular_number():
    """
    Tweak the value of "linit" until the divisors list has length > 500.
    """
    for i in range(10000000):
        nth_triangular_num = triangular_number(i)
        divisors = get_divisors(nth_triangular_num)
        num_divisors = len(divisors)
        # print(num_divisors)
        if num_divisors > 500:
            return nth_triangular_num
    return -1


def triangular_number(n, acc=1):
    """
    While computing triangular numbers can be done purely recursively, but you will run into
    a stack overflow error. Therefore, you'll have to convert it into an iterative algorithm.

    See this as well: http://blog.moertel.com/posts/2013-05-11-recursive-to-iterative.html
    """
    while n > 1:
        (n, acc) = (n - 1, acc + n)
    return acc


def get_divisors(n):
    """
    Optimizations:
    - compute pairs of divisors at each iteration
    - only need to iterate up to the square root of n
    """
    divisors = []
    limit = math.ceil(math.sqrt(n))
    for i in range(1, limit):
        if n % i == 0:
            dividend = n // i
            if dividend == i:
                divisors.append(i)
            else:
                divisors.append(i)
                divisors.append(dividend)
    return divisors


if __name__ == "__main__":
    answer = highly_divisble_triangular_number()
    print(answer)

