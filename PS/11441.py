import sys

# 수의 개수 N
N = int(sys.stdin.readline().strip())

ary = list(map(int, sys.stdin.readline().split()))

# ary를 누적합 배열로 수정
for i in range(N - 1):
    ary[i + 1] += ary[i]

# 구간의 개수 M
M = int(sys.stdin.readline().strip())

# 구간 합 구하기 시작 (1 ≤ i ≤ j ≤ N)
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())

    if i == 1:
        print(ary[j - 1])
    elif i == j:
        print(ary[i - 1] - ary[i - 2])
    else:
        print(ary[j - 1] - ary[i - 2])
