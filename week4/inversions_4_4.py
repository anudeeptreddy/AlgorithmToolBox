# Uses python3
import sys


def merge_lists(a, b, left, mid, right):
    # Makes a merged list in sorted order from given lists & calculates number of inversion required.
    left_list = left
    right_list = mid
    merged_list = left
    inversion_count = 0

    while left_list <= mid - 1 and right_list <= right:
        if a[left_list] <= a[right_list]:
            b[merged_list] = a[left_list]
            merged_list += 1
            left_list += 1
        else:
            b[merged_list] = a[right_list]
            merged_list += 1
            right_list += 1
            # (mid - left_list) are the number of inversions required once
            # an element is identified in left list that is greater than the right list element
            inversion_count = inversion_count + (mid - left_list)

    while left_list <= mid-1:   # append remaining left list elements
        b[merged_list] = a[left_list]
        merged_list += 1
        left_list += 1

    while right_list <= right:   # append remaining right list elements
        b[merged_list] = a[right_list]
        merged_list += 1
        right_list += 1

    for i in range(left, right+1):   # update input array a with result b (i.e merged & sorted)
        a[i] = b[i]

    return inversion_count


def get_number_of_inversions(a, b, left, right):
    # Algorithm to determine the number of inversion required to make the list a sorted list
    # using merge sort algorithm.
    number_of_inversions = 0
    if left < right:
        ave = (left + right) // 2
        number_of_inversions += get_number_of_inversions(a, b, left, ave)
        number_of_inversions += get_number_of_inversions(a, b, ave+1, right)
        number_of_inversions += merge_lists(a, b, left, ave+1, right)
    return number_of_inversions


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)-1))