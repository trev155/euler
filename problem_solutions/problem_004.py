"""
Problem 4 - Largest Palindrome Product
https://projecteuler.net/problem=4
"""


def largest_palindrome_product():
    # find candidates from 100*100 to 999*999
    candidates = []
    for i in range(10000, 998001):
        if is_palindrome(i):
            candidates.append(i)
    # print(candidates)

    # for each candidate, see if it can be factorized into 2 three-digit numbers
    candidates.reverse()
    for candidate in candidates:
        if three_digit_factorization(candidate):
            return candidate

    # should never get here
    return -1


def is_palindrome(n):
    s = str(n)
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True


def three_digit_factorization(n):
    for i in range(100, 1000):
        if n % i == 0:
            f = n // i
            if len(str(f)) == 3:
                # print(i, f)
                return True
    return False


if __name__ == "__main__":
    answer = largest_palindrome_product()
    print(answer)
