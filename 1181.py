ary = []
N = int(input())

for i in range(N):
    tmp = input()
    ary.append(tmp)

# remove duplicate
def remove_dup(ary):
    set_ary = set(ary)
    return list(set_ary)

# bubble sort
def bubble_sort(ary):
    for i in range(len(ary)):
        for j in range(1, len(ary) - i):
            if (len(ary[j - 1]) > len(ary[j])):
                tmp = ary[j]
                ary[j] = ary[j - 1]
                ary[j - 1] = tmp
    return ary

# 사전식 정렬 구현하기 -> sorted? 가능

# 사용 순서는 아래와 같다
# 1. set 사용해 중복 제거
# 2. sorted 사용해 사전순으로 정렬
# 3. bubble sort 사용해 길이 순으로 정렬

remove_dup_ary = remove_dup(ary)
dict_sort_ary = sorted(remove_dup_ary)
remove_dup_bubble_sort_ary = bubble_sort(dict_sort_ary)

for str in remove_dup_bubble_sort_ary:
    print(str)
