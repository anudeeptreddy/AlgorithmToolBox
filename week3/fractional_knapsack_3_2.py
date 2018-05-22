# Uses python3
import sys


def get_optimal_value(capacity, weights, values):

    # algorithm to calculate maximum value of a knapsack
    value_per_unit = [v/y for v, y in zip(values, weights)]
    vpu_weight_value = zip(value_per_unit, weights, values)

    # sort items by value per unit
    vpu_weight_value_sorted = sorted(vpu_weight_value, key=lambda x: x[0], reverse=True)
    max_value_of_knapsack = 0

    for item_tuple in vpu_weight_value_sorted:
        if capacity == 0:
            return max_value_of_knapsack

        available_capacity = min(item_tuple[1], capacity)
        max_value_of_knapsack = max_value_of_knapsack + available_capacity*item_tuple[0]

        capacity = capacity - available_capacity

    return max_value_of_knapsack


if __name__ == "__main__":
    # print get_optimal_value(50, [20, 50, 30], [60, 100, 120])
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))


'''
i/p:
3 50
60 20
100 50
120 30
o/p:
180.00
'''