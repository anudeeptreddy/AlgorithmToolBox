# Uses python3

import sys


def max_dot_product(a, b):
    # Algorithm to maximize sum of proudcts of a[i] and b[i]
    sorted_a = sorted(a)
    sorted_b = sorted(b)
    return sum([x*y for x, y in zip(sorted_a, sorted_b)])


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))

