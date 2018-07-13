"""
Problem 17 - Number Letter Counts
https://projecteuler.net/problem=17
"""


def number_letter_counts():
    total_letters = 0
    i = 1
    while i <= 1000:
        total_letters += num_letters(i)
        i += 1
    return total_letters


def num_letters(i):
    letters = 0

    hundreds = i // 100
    tens = (i % 100) // 10
    ones = (i % 100) % 10

    # thousand
    if i == 1000:
        # one thousand = 11 letters
        letters += 11
    else:
        # hundreds
        if hundreds > 0 and hundreds < 10:
            if hundreds in [1, 2, 6]:
                # (one, two, six) hundred and = 13 letters
                letters += 13
            if hundreds in [3, 7, 8]:
                # (three, seven, eight) hundred and = 15 letters
                letters += 15
            if hundreds in [4, 5, 9]:
                # (four, five, nine) hundred and = 14 letters
                letters += 14
            if tens == 0 and ones == 0:
                # get rid of the "and"
                letters -= 3

        # tens, ones
        if tens == 1:
            if ones == 0:
                letters += 3
            if ones in [1, 2]:
                letters += 6
            if ones in [3, 4, 8, 9]:
                letters += 8
            if ones in [5, 6]:
                letters += 7
            if ones in [7]:
                letters += 9
        else:
            if tens in [2, 3, 8, 9]:
                letters += 6
            if tens in [4, 5, 6]:
                letters += 5
            if tens in [7]:
                letters += 7

            if ones in [1, 2, 6]:
                letters += 3
            if ones in [3, 7, 8]:
                letters += 5
            if ones in [4, 5, 9]:
                letters += 4

    print(i, letters)
    return letters


if __name__ == "__main__":
    answer = number_letter_counts()
    print(answer)
