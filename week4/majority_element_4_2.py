# Uses python3
import sys


def get_me_frequency(a, majority_element, left, right):
    frequency = 0
    for i in range(left, right+1):
        if a[i] == majority_element:
            frequency += 1
    return frequency


def get_majority_element(a, left, right):
    # Divide and conquer algorithm to determine if a max element exists
    # i.e a number that occurs at least n/2 time where n is length of the list
    if left > right: return -1
    if left == right: return a[left]

    mid = left + (right - left)//2

    left_me = get_majority_element(a, left, mid)
    right_me = get_majority_element(a, mid+1, right)

    left_me_frequency = get_me_frequency(a, left_me, left, right)
    if left_me_frequency > ((right - left)+1) // 2:
        return left_me

    right_me_frequency = get_me_frequency(a, right_me, left, right)
    if right_me_frequency > ((right - left)+1) // 2:
        return right_me

    return -1


def get_majority_element_linear(a):
    # Algorithm to determine if a majority element exists in linear time
    # scan 1 finds frequency scan 2 checks if a majority element exists
    freq_count = {}
    for num in a:
        if num in freq_count.keys():
            freq_count[num] = freq_count[num]+1
        else:
            freq_count[num] = 1
    for freq in freq_count.values():
        if freq > len(a)/2:
            return 1
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n-1) != -1:
        print(1)
    else:
        print(0)
