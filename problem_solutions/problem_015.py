"""
Problem 15 - Lattice Paths
https://projecteuler.net/problem=15
"""


def lattice_paths(r, d):
    """
    r represents the number of times we must move right to reach the goal
    d represents the number of time we must move down to reach the goal
    """
    # check if already seen
    if (r, d) in paths:
        return paths[(r, d)]

    # base cases
    if r == 0 and d == 0:
        paths[(r, d)] = 0
    elif r == 0:
        paths[(r, d)] = 1
    elif d == 0:
        paths[(r, d)] = 1
    # recursive case
    else:
        paths[(r, d)] = lattice_paths(r - 1, d) + lattice_paths(r, d - 1)

    return paths[(r, d)]


if __name__ == "__main__":
    paths = {}
    answer = lattice_paths(20, 20)
    print(answer)
