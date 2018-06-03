# Uses python3
import sys
import random


def partition3(a, l, r):
    # Three partition quick sort algorithm
    # partition 1 : all elements less than pivot (left most partition)
    # partition 2 : all elements equal to pivot (center partition)
    # partition 3 : all elements greater than pivot (right most partition)
    pivot_element = a[l]
    i = l+1     # iterate from start of list to beginning of partition 3
    j = l
    k = r
    while i <= k:
        if a[i] < pivot_element:
            a[i], a[j] = a[j], a[i]
            j += 1
            i += 1
        elif a[i] > pivot_element:
            a[i], a[k] = a[k], a[i]
            k -= 1
        else:
            i += 1
    return j, k


def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
