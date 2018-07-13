"""
Problem 13 - Large Sum
https://projecteuler.net/problem=13
"""


def large_sum():
    # read in the data file
    with open("problem_013_data.txt") as file:
        data = list(map(lambda l: l.strip(), file.readlines()))

    # column-wise addition (from the LSB to the MSB)
    size = len(data[0])
    result = []
    carry = 0
    for c in range(size):
        acc = 0

        for num in data:
            acc += int(num[size - 1 - c])
        acc += carry

        digit = acc % 10
        carry = acc // 10
        result.append(digit)

        if c == size - 1:
            while carry > 10:
                result.append(carry // 10)
                carry = carry % 10
            result.append(carry)

    # process the result
    first_ten_digits = []
    for i in range(1, 11):
        first_ten_digits.append(str(result[-i]))
    first_ten_digits = "".join(first_ten_digits)
    return int(first_ten_digits)


if __name__ == "__main__":
    answer = large_sum()
    print(answer)

