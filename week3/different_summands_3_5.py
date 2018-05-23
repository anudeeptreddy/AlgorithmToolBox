# Uses python3
import sys


def optimal_summands(n):
    summands = []
    # algorithm to convert a positive number into as many individual positive numbers as possible
    total_value = n
    allot_value = 1
    while total_value:
        if total_value <= 2*allot_value:
            summands.append(total_value)
            return summands
        else:
            summands.append(allot_value)
            total_value -= allot_value
            allot_value += 1
    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
