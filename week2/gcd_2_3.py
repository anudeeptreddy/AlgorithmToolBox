# Uses python3
import sys


def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd_euclid(a, b):
    if b == 0:
        return a
    if a >= b > 0:
        return gcd_euclid(b, a%b)
    elif b >= a > 0:
        return gcd_euclid(a, b%a)



if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_euclid(a, b))
