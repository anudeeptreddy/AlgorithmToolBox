# Uses python3
import sys


def optimal_weight(W, w):
    # Algorithm for knapsac problem without any repetitions
    # All the weights have identical value
    result = [0] * (W + 1)
    n = len(w)

    # We calculate the max value possible for all the possible weights increasing one possible weight every iteration
    for i in range(n):
        for j in range(W, w[i]-1, -1):                          # iterate from max weight until the weight
            result[j] = max(result[j], result[j-w[i]] + w[i])   # since value = weight, we add weight as value

    return result[W]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
