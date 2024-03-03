import sys


def bubble_sort(num_list):
    for i in range(0, len(num_list)):
        for j in range(1, len(num_list) - i):
            if num_list[j] < num_list[j - 1]:
                tmp = num_list[j]
                num_list[j] = num_list[j - 1]
                num_list[j - 1] = tmp
    return num_list


def quick_sort(num_list):
    if len(num_list) <= 1:
        return num_list

    pivot = num_list[0]
    left, right, equal = [], [], []

    for i in range(0, len(num_list)):
        if num_list[i] > pivot:
            right.append(num_list[i])
        elif num_list[i] < pivot:
            left.append(num_list[i])
        elif num_list[i] == pivot:
            equal.append(num_list[i])

    left_recursion = quick_sort(left)
    right_recursion = quick_sort(right)

    return left_recursion + equal + right_recursion


def merge_sort(num_list):
    # divide
    if len(num_list) < 2:
        return num_list
    mid = len(num_list) // 2

    left_ary = merge_sort(num_list[:mid])
    right_ary = merge_sort(num_list[mid:])

    # conquer
    merged_ary = []
    l = r = 0
    while l < len(left_ary) and r < len(right_ary):
        if left_ary[l] < right_ary[r]:
            merged_ary.append(left_ary[l])
            l += 1
        else:
            merged_ary.append(right_ary[r])
            r += 1
    merged_ary += left_ary[l:]
    merged_ary += right_ary[r:]
    return merged_ary


N = int(sys.stdin.readline())

ary = []

for _ in range(N):
    tmp = int(sys.stdin.readline())
    ary.append(tmp)

sorted_ary = merge_sort(ary)

# sorted_ary = sorted(ary)

for num in sorted_ary:
    sys.stdout.write(str(num) + "\n")
