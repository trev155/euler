"""
Problem 2 - Even Fibonacci Numbers
https://projecteuler.net/problem=2
"""
def even_fibonacci_numbers():
    fib(50)

    vals = list([v for k, v in fib_terms.items()])
    sum = 0
    for val in vals:
        if val % 2 == 0 and val < 4000000:
            sum += val
    return sum

fib_terms = {}

def fib(n):
    if n == 1:
        fib_terms[n] = 1
        return 1
    if n == 2:
        fib_terms[n] = 2
        return 2
    # check if already stored
    if n in fib_terms:
        return fib_terms[n]
    else:
        result = fib(n-2) + fib(n-1)
        fib_terms[n] = result
        return result


if __name__ == "__main__":
    answer = even_fibonacci_numbers()
    print(answer)
