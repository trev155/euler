"""
Problem 3 - Largest Prime Factor
https://projecteuler.net/problem=3
"""


def largest_prime_factor(n):
    """
    Procedure:
    1. initialize a "factor list", at the start it only contains n
    2. Repeatedly attempt to break down each element in the factor list into smaller and smaller factors,
    until we only end up with prime factors.
    3. Do this by iterating from 2 to n // 2, and testing if n % i == 0
    - if 0 remainder, add the factors to the factor list. otherwise, n was a prime factor
    4. keep track of all of these prime factors. return the largest of them
    """
    factor_list = [n]
    prime_factors = []
    while len(factor_list) > 0:
        n = factor_list[0]
        factor_list.remove(n)
        result = helper(n)
        if result[0] is None:
            prime_factors.append(result[1])
        else:
            factor_list = factor_list + result[0]
    return max(prime_factors)


def helper(n):
    """
    Return a tuple of either:
    - (None, prime factor)
    - ([2 new factors], None)

    The first case is if n does not factorize into anything., in which case we want to keep track of this prime factor.
    The second case is if n does factorize, in which case we want to add it to our factor list.
    """
    for i in range(2, n // 2):
        if n % i == 0:
            f = n // i
            return ([f, i], None)
    return (None, n)


if __name__ == "__main__":
    answer = largest_prime_factor(600851475143)
    print(answer)
