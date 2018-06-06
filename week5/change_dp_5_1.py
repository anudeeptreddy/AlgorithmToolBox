# Uses python3
import sys


def get_change(money):
    # Algorithm to calculate minimum number of coins required to match a given change
    coins = [1, 3, 4]
    money = money + 1   # To accommodate money value 0
    min_num_coins = [float('inf')] * money

    min_num_coins[0] = 0
    for m in range(1, money):
        for i in range(len(coins)):
            if m >= coins[i]:
                num_coins = min_num_coins[m-coins[i]] + 1
                if num_coins < min_num_coins[m]:
                    min_num_coins[m] = num_coins
    return min_num_coins[m]


if __name__ == '__main__':
    money = int(sys.stdin.read())
    print(get_change(money))
