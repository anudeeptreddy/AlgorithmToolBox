# Uses python3
import sys


def get_change(m):
    # return minimum number of coins for given money
    rem_value = m
    total_coins = 0
    denominations = [10, 5, 1]
    for value in denominations:
        if rem_value and (rem_value/value) >= 1:
            total_coins += int(rem_value/value)
            rem_value = rem_value % value
    return total_coins


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
