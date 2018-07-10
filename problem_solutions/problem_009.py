"""
Problem 9 - Special Pythagorean Triplet
https://projecteuler.net/problem=9
"""


def special_pythagorean_triplet():
    for a in range(333):
        for b in range(a, 500):
            c = 1000 - a - b
            c_sq = c*c
            a_sq_b_sq = a*a + b*b
            if c_sq == a_sq_b_sq:
                print(a, b, c)
                print(a_sq_b_sq)
                print(c_sq)
                print("------")
                return a * b * c
    return -1


if __name__ == "__main__":
    answer = special_pythagorean_triplet()
    print(answer)
