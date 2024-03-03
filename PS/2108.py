import collections

# 산술평균 반환 함수
def arithmetic_mean(num_list):
    sum = 0
    for num in num_list:
        sum += num
    # 소수점 첫째 반올림을 하기 위해 파이썬에 내장된 round() 함수를 사용
    return round(sum / len(num_list))

# 중앙값 반환 함수
def median(num_list):
    sorted_num_list = sorted(num_list)
    idx = len(num_list) // 2
    return sorted_num_list[idx]

# (중요) 최빈값 반환 함수
def mode(num_list):
    sorted_num_list = sorted(num_list)
    # collections.Counter(a).most_common(n) : a의 요소들을 세어, 최빈값 n개를 반환한다
    # 즉 아래 코드는 오름차순 정렬된 num_list에서 최빈값 2개를 반환하는 코드이다.
    mode = collections.Counter(sorted_num_list).most_common(2)

    if (N > 1):
        # 반환된 두 개의 최빈값의 크기가 같다면 두 번째로 작은 최빈값을 반환하라는 조건
        if (mode[0][1] == mode[1][1]):
            return mode[1][0] # 크기가 같으면 두번째꺼 반환
        else:
            return mode[0][0] # 크기가 다르면 첫번째꺼 반환
    else:
        return mode[0][0]


def num_range(num_list):
    max_num = max(num_list)
    min_num = min(num_list)
    return max_num - min_num

N = int(input())
num_list = []
for i in range(N):
    num_list.append(int(input()))

print(arithmetic_mean(num_list))
print(median(num_list))
print(mode(num_list))
print(num_range(num_list))