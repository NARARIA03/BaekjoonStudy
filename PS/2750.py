from sys import stdin


def merge_sort(num_ary):
    if len(num_ary) < 2:
        return num_ary

    mid = len(num_ary) // 2

    left = merge_sort(num_ary[:mid])
    right = merge_sort(num_ary[mid:])

    l = r = 0
    merged_ary = []
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            merged_ary.append(left[l])
            l += 1
        else:
            merged_ary.append(right[r])
            r += 1

    merged_ary += left[l:]
    merged_ary += right[r:]
    return merged_ary


N = int(stdin.readline().rstrip())
ary = []

for _ in range(N):
    num = int(stdin.readline().rstrip())
    ary.append(num)

res_ary = merge_sort(ary)

for item in res_ary:
    print(item)
