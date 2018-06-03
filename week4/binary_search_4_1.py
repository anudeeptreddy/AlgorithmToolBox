# Uses python3
import sys


def binary_search(a, x):
    # Algorithm to implement binary search using non recursive approach
    # Picks a key & looks for it either in the left half or right half if the key is not in the center
    # Works only on sorted list
    left, right = 0, len(a)-1
    while right >= left:
        mid = int((left + right) / 2) if right != left else left
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, x), end = ' ')
