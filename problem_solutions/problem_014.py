"""
Problem 14 - Longest Collatz Sequence
https://projecteuler.net/problem=14
"""


def longest_collatz_sequence():
    longest_seq = -1
    longest_seq_start = -1
    for i in range(1000000):
        sequence = collatz(i)
        seq_len = len(sequence)
        if seq_len > longest_seq:
            longest_seq = seq_len
            longest_seq_start = i
    return longest_seq_start


def collatz(start):
    sequence = []
    while start > 1:
        sequence.append(start)
        if start % 2 == 0:
            start = start // 2
        else:
            start = (start * 3) + 1
    sequence.append(start)
    return sequence


if __name__ == "__main__":
    answer = longest_collatz_sequence()
    print(answer)
