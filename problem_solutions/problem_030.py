"""
Problem 30 - Digit Fifth Powers
https://projecteuler.net/problem=30
"""
import math


def fifth_powers():
    nums = []
    # each digit can give you at max 9^5 to your sum, so we don't have to iterate through anything past 6 digits
    for i in range(2, 300000):
        i_str = str(i)
        power_sum = 0
        for c in i_str:
            power_sum += int(math.pow(int(c), 5))
        if i == power_sum:
            nums.append(i)
    # print(nums)
    return sum(nums)


if __name__ == "__main__":
    answer = fifth_powers()
    print(answer)