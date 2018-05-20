# Uses python3
import sys


def get_fibonacci_last_digit_naive(n):
    lst = [0, 1]
    if n <= 1:
        return lst[n]
    for i in list(range(2, n+1)):
        lst.append((lst[i-1]+lst[i-2]) % 10)

    return lst[n]


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
