# Uses python3
import sys


def optimal_sequence_dp(n):
    # Algorithm to compute the minimum number of operations needed to obtain the number n starting from 1.
    # Permissible operations for the current number x are: x * 2 (or) x * 3 (or) x + 1
    sequence = []

    no_of_ops_to_i = [0] * (n+1)   # Needed to accommodate the result 0
    # no_of_ops_to_i holds the minimum number of operations required to arrive at index i using above operations
    for i in range(1, len(no_of_ops_to_i)):
        no_of_ops_to_i[i] = no_of_ops_to_i[i - 1] + 1
        if i % 2 == 0:
            no_of_ops_to_i[i] = min(no_of_ops_to_i[i // 2] + 1, no_of_ops_to_i[i])
        if i % 3 == 0:
            no_of_ops_to_i[i] = min(no_of_ops_to_i[i // 3] + 1, no_of_ops_to_i[i])

    # Backtracking the logic above to reconstruct the sequence of numbers
    while n > 1:
        sequence.insert(0, n)
        # Determining the next element in sequence
        if no_of_ops_to_i[n - 1] == no_of_ops_to_i[n] - 1:
            n = n - 1
        elif n % 2 == 0 and no_of_ops_to_i[n // 2] == no_of_ops_to_i[n] - 1:
            n = n // 2
        elif n % 3 == 0 and no_of_ops_to_i[n // 3] == no_of_ops_to_i[n] - 1:
            n = n // 3
    sequence.insert(0, 1)
    return sequence


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence_dp(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
