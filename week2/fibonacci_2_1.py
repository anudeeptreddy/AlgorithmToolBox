# Uses python3
memoize = {}


def calc_fib(n):
    if n in memoize.keys():
        return memoize[n]
    if (n <= 1):
        return n
    res = calc_fib(n - 2) + calc_fib(n - 1)
    memoize[n] = res
    return res


n = int(input())
print(calc_fib(n))

