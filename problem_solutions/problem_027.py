"""
Problem 27 - Quadratic Primes
https://projecteuler.net/problem=27
"""


def quadratic_primes():
    return -1


def is_prime(n):
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            return False
    return True


def formula(n, a, b):
    return n*n + a*n + b


if __name__ == "__main__":
    answer = quadratic_primes()
    print(answer)