"""
Problem 7 - 10001st Prime
https://projecteuler.net/problem=7
"""


class MarkedNumber:
    def __init__(self, val):
        self.val = val
        self.visited = False


def sieve(high=2000000):
    """
    Implementation of the Sieve of Eratosthenes algorithm.

    This is similar to my implementation of Problem 10 (Prime summation), which I completed before this one.
    Basically, I generate a list of all the prime numbers up until a point (marked by the "high" value).
    After that, simply take the 10001st value in this list.

    The "high" value should be set to a number high enough to generate enough primes.
    """
    lst = [MarkedNumber(i) for i in range(high)]
    p = 1
    while True:
        # find the next prime
        found_prime = False
        for i in range(p, high):
            num = lst[i]
            if num.val > p and not num.visited:
                p = num.val
                found_prime = True
                break
        if not found_prime:
            break
        # mark multiples of p as visited, but not p itself
        current = p * 2
        while current < high:
            lst[current].visited = True
            current = current + p

    primes = list(filter(lambda x: not x.visited, lst))
    primes = list(map(lambda x: x.val, primes))
    # remove 0 and 1 from the prime numbers list
    del primes[0]
    del primes[0]
    return primes[10000]


if __name__ == "__main__":
    answer = sieve()
    print(answer)
