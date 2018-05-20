# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a)==n)

n1 = max(a)
a.remove(n1)
n2 = max(a)
a.remove(n2)
print(n1*n2)