"""
Problem 31 - Coin Sums
https://projecteuler.net/problem=31
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

    def __repr__(self):
        return "Node: %s" % self.val


def coin_sums():
    coins = [1, 5, 10]

    x = coin_helper(coins, 200)
    print(x)

    y = traversal(x, [])
    print(y)

    # now go through each path and convert it into a set of coins, see how many unique paths there are
    coin_combinations = []
    for path in y:
        pass

    return -1


def coin_helper(coins, target):
    """
    coins is a list of ints, guaranteed to contain at least the value of 1
    target is an int, the value we want to make
    """
    if target == 0:
        return Node(target)

    root = Node(target)
    for coin in coins:
        if coin <= target:
            child = coin_helper(coins, target - coin)
            root.children.append(child)
    return root


def traversal(root, seen):
    # no children
    if len(root.children) == 0:
        return [seen + [root.val]]

    all_paths = []
    for child in root.children:
        paths = traversal(child, seen)
        for path in paths:
            all_paths.append([root.val] + path)
    return all_paths


if __name__ == "__main__":
    answer = coin_sums()
    print(answer)