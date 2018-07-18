"""
Problem 22 - Names Scores
https://projecteuler.net/problem=22
"""


def names_scores():
    # open data file and read it in sorted
    with open("problem_022_data.txt") as file:
        names = file.readlines()[0]
        names = names.replace('"', '').split(",")
        names.sort()

    # compute scores
    scores = [compute_score(names[i], i + 1) for i in range(len(names))]
    return sum(scores)


def compute_score(s, position):
    # compute score of a name string, as specified by the question
    # assumption: string is in all caps
    score = 0
    for c in s:
        char_score = ord(c) - 64
        score += char_score
    return score * position


if __name__ == "__main__":
    answer = names_scores()
    print(answer)
