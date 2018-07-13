"""
Problem 16 - Power Digit Sum
https://projecteuler.net/problem=16
"""


def power_digit_sum():
    """
    You can't represent 2^1000 using built in types, so instead I use a list of digits instead, and perform
    repeated multiplication over the digits of the list.

    The list is a fixed size that should be large enough to store the value 2^1000.
    On each iteration, go through each list element and double it, making sure to keep track of carry over values.

    eg)
    [1, 0, 0, 0]
    [2, 0, 0, 0]
    [4, 0, 0, 0]
    [8, 0, 0, 0]
    [6, 1, 0, 0]
    [2, 3, 0, 0]
    etc.
    """
    arr = [0] * 1000
    arr[0] = 1
    num_digits = 1
    for i in range(1000):
        carry = 0
        for e in range(num_digits):
            digit = arr[e]
            if digit < 5:
                arr[e] = digit * 2
                arr[e] += carry
                carry = 0
            else:
                arr[e] = (digit * 2) % 10
                arr[e] += carry
                carry = 1
                if e == num_digits - 1:
                    num_digits += 1
                    arr[e + 1] = 1

    return sum(arr)


if __name__ == "__main__":
    answer = power_digit_sum()
    print(answer)
