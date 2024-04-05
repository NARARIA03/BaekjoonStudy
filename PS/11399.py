import sys


def merge_sort(ary):
    if len(ary) < 2:
        return ary

    m = len(ary) // 2
    left = merge_sort(ary[:m])
    right = merge_sort(ary[m:])

    l = r = 0
    res_ary = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            res_ary.append(left[l])
            l += 1
        else:
            res_ary.append(right[r])
            r += 1
    res_ary += left[l:]
    res_ary += right[r:]
    return res_ary


N = int(sys.stdin.readline().strip())
p_ary = list(map(int, sys.stdin.readline().split()))
sorted_p_ary = merge_sort(p_ary)

result = 0
hap = 0
for i in range(N):
    hap += sorted_p_ary[i]
    result += hap
print(result)
