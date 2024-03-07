def merge_sort(num_list):
    if len(num_list) < 2:
        return num_list
    mid = len(num_list) // 2
    left = merge_sort(num_list[:mid])
    right = merge_sort(num_list[mid:])

    i = j = 0
    merged_list = []
    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            merged_list.append(left[i])
            i += 1
        elif left[i][0] > right[j][0]:
            merged_list.append(right[j])
            j += 1
        elif left[i][1] < right[j][1]:
            merged_list.append(left[i])
            i += 1
        elif left[i][1] > right[j][1]:
            merged_list.append(right[j])
            j += 1

    merged_list += left[i:]
    merged_list += right[j:]
    return merged_list


N = int(input())
num_list = [list(map(int, input().split())) for _ in range(N)]

sorted_num_list = merge_sort(num_list)

for i in range(N):
    print(sorted_num_list[i][0], sorted_num_list[i][1])
