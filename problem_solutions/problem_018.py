"""
Problem 18 - Maximum Path Sum 1
https://projecteuler.net/problem=18
"""


def max_path_sum():
    # read in data
    with open("problem_018_data.txt") as file:
        data = []
        for line in file:
            line = line.strip().split(" ")
            line = list(map(lambda x: Node(int(x)), line))
            data.append(line)

    # build a tree
    for i in range(len(data) - 1):
        for j in range(len(data[i])):
            data[i][j].left = data[i+1][j]
            data[i][j].right = data[i+1][j+1]

    # traverse the tree for the best path
    root = data[0][0]
    val = best_path(root)

    return val


def best_path(node):
    """
    Compute the value of the best path of the tree starting at node.
    """
    if node.left is None and node.right is None:
        return node.val
    else:
        best_left = node.val + best_path(node.left)
        best_right = node.val + best_path(node.right)
        return max(best_left, best_right)


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return "Node " + str(self.val)


if __name__ == "__main__":
    answer = max_path_sum()
    print(answer)
