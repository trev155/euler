"""
Problem 1 - Multiples of 3 and 5
https://projecteuler.net/problem=1
"""
def multiples_of_3_and_5(n):
    sum = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

if __name__ == "__main__":
    answer = multiples_of_3_and_5(1000)
    print(answer)
