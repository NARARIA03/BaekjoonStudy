def merge_sort(ary):
    if len(ary) < 2:
        return ary

    mid = len(ary) // 2
    left = ary[:mid]
    right = ary[mid:]
    left_ary = merge_sort(left)
    right_ary = merge_sort(right)

    merged_ary = []
    l = r = 0
    while l < len(left_ary) and r < len(right_ary):
        if left_ary[l][0] <= right_ary[r][0]:
            merged_ary.append(left_ary[l])
            l += 1
        else:
            merged_ary.append(right_ary[r])
            r += 1
    merged_ary += left_ary[l:]
    merged_ary += right_ary[r:]
    return merged_ary


N = int(input())

ary = [[0 for _ in range(2)] for _ in range(N)]

for i in range(N):
    num, name = map(str, input().split())
    ary[i][0] = int(num)
    ary[i][1] = name

sorted_ary = merge_sort(ary)

for i in range(N):
    print(sorted_ary[i][0], sorted_ary[i][1])
