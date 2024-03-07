def merge_sort(ary):
    if len(ary) < 2:
        return ary

    mid = len(ary) // 2
    left = merge_sort(ary[:mid])
    right = merge_sort(ary[mid:])

    merged_ary = []
    l = r = 0

    while l < len(left) and r < len(right):
        if left[l][1] < right[r][1]:
            merged_ary.append(left[l])
            l += 1
        elif left[l][1] > right[r][1]:
            merged_ary.append(right[r])
            r += 1
        elif left[l][0] < right[r][0]:
            merged_ary.append(left[l])
            l += 1
        else:
            merged_ary.append(right[r])
            r += 1
    merged_ary += left[l:]
    merged_ary += right[r:]
    return merged_ary


N = int(input())
xy_ary = [list(map(int, input().split())) for _ in range(N)]

sorted_xy_ary = merge_sort(xy_ary)

for i in range(N):
    print(sorted_xy_ary[i][0], sorted_xy_ary[i][1])
