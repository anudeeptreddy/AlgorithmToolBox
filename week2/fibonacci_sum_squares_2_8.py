# Uses python3
from sys import stdin


def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

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


def fibonacci_sum_squares_optimal(n):
    # last digit can be achieved by modulo 10
    fibonacci = [0, 1]
    f = lambda x: (x*x) % 10
    pisano_period = get_pisano_period(10)
    nth_fib = n % pisano_period
    for i in list(range(2, nth_fib+1)):
        fibonacci.append((fibonacci[i-1]+fibonacci[i-2]) % 10)
    fibonacci = [f(x) for x in fibonacci]
    return sum(fibonacci) % 10 if nth_fib != 0 else 0


if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_optimal(n))
