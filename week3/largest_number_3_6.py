# Uses python2

import sys


def custom_compare(x, y):
    x, y = str(x), str(y)
    xy, yx = x+y, y+x
    if xy == yx:
        return 0
    return -1 if xy < yx else 1


def largest_number(a):
    # sort a list to form a largest number
    a.sort(cmp=custom_compare, reverse=True)
    return ''.join(a)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print (largest_number(a))

