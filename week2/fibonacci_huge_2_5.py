# Uses python2
import sys


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def get_pisano_period(m):
    n1 = 0
    n2 = 1
    # pisano period cannot me more than m times m
    for period_length in range(m*m):
        n1, n2 = n2, (n1+n2) % m
        # pisano periods always starts with 0 1
        if n1 == 0 and n2 == 1:
            return period_length + 1


def get_fibonacci_optimal(n, m):
    fibonacci = [0, 1]
    pisano_period = get_pisano_period(m)
    nth_fib = n % pisano_period
    for i in list(range(2, nth_fib+1)):
        fibonacci.append((fibonacci[i-1]+fibonacci[i-2]) % m)
    return fibonacci[nth_fib]


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_optimal(n, m))
