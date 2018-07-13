"""
Problem 11 - Largest Product in a Grid
https://projecteuler.net/problem=11
"""
import numpy as np


def largest_grid_product():
    """
    The idea here is to use numpy and the np.diagonal() function to retrieve all the diagonals of an np array.
    """
    # read in file
    data_arr = []
    with open("problem_011_data.txt") as data:
        for line in data:
            arr = line.strip().split(" ")
            data_arr.append(arr)

    # -- process all the directions
    best_product = -1
    data = np.array(data_arr)
    inversed_data = data[::-1, :]
    transposed_data = data.T

    # get the diagonals
    bot_left_up_right = get_bottom_left_to_top_right_diagonals(data)
    up_left_bot_right = get_bottom_left_to_top_right_diagonals(inversed_data)

    # process all the diagonals
    all_diagonals = bot_left_up_right + up_left_bot_right
    best_product = -1
    for d in all_diagonals:
        if len(d) > 3:
            l = d.astype(np.int)
            for i in range(len(l) - 3):
                product = l[i] * l[i+1] * l[i+2] * l[i+3]
                if product > best_product:
                    best_product = product

    # process all the rows
    for r in data:
        for i in range(len(r) - 3):
            l = r.astype(np.int)
            product = l[i] * l[i + 1] * l[i + 2] * l[i + 3]
            if product > best_product:
                best_product = product

    # process all columns
    for r in transposed_data:
        for i in range(len(r) - 3):
            l = r.astype(np.int)
            product = l[i] * l[i + 1] * l[i + 2] * l[i + 3]
            if product > best_product:
                best_product = product

    return best_product


def get_bottom_left_to_top_right_diagonals(arr):
    """
    Given a numpy array arr, return all the diagonals (from top left, moving to the bottom right corner) as a list of
    numpy arrays.
    """
    diagonals = [arr.diagonal(i) for i in range(-arr.shape[0] + 1, arr.shape[1])]
    return diagonals


if __name__ == "__main__":
    answer = largest_grid_product()
    print(answer)

