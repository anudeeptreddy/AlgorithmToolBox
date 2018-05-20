# Uses python3
import sys


def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


def get_pisano_period(m):
    n1 = 0
    n2 = 1
    # pisano period cannot me more than m times m
    for period_length in range(m*m):
        n1, n2 = n2, (n1+n2) % m
        # pisano periods always starts with 0 1
        if n1 == 0 and n2 == 1:
            return period_length + 1


def fibonacci_partial_sum_optimal(m, n):
    # last digit can be achieved by modulo 10
    fibonacci = [0, 1]
    pisano_period = get_pisano_period(10)
    mth_fib = m % pisano_period
    nth_fib = n % pisano_period
    for i in list(range(2, nth_fib+1)):
        fibonacci.append((fibonacci[i-1]+fibonacci[i-2]) % 10)
    return sum(fibonacci[mth_fib:]) % 10 if nth_fib != 0 else 0


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_optimal(from_, to))