# Uses python2
import sys


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


def gcd_euclid(a, b):
    if b == 0:
        return a
    if a >= b > 0:
        return gcd_euclid(b, a%b)
    elif b >= a > 0:
        return gcd_euclid(a, b%a)


def lcm_optimal(a, b):
    return long((a*b)/gcd_euclid(a, b))


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_optimal(a, b))

