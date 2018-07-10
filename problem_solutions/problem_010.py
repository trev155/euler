"""
Problem 10 - Summation of Primes
https://projecteuler.net/problem=10
"""


class MarkedNumber:
    def __init__(self, val):
        self.val = val
        self.visited = False


def summation_primes():
    """
    Implementation of the Sieve of Eratosthenes algorithm.
    """
    high = 2000000
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
    return sum(primes)


if __name__ == "__main__":
    answer = summation_primes()
    print(answer)
