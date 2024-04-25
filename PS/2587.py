def merge_sort(num_ary: list):
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


def print_mean(num_ary: list):
    sum = 0
    for num in num_ary:
        sum += num
    print(sum // len(num_ary))


num_ary = []
for _ in range(5):
    num = int(input())
    num_ary.append(num)
sorted_num_ary = merge_sort(num_ary)
print_mean(sorted_num_ary)
print(sorted_num_ary[len(sorted_num_ary) // 2])
