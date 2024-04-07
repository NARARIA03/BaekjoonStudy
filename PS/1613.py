import sys

n, k = map(int, sys.stdin.readline().split())
INF = float("inf")
ary = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

# ary[i][j] ==> i 사건이 j 사건보다 먼저 일어났다는 의미
for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    ary[a][b] = 1

# 플로이드-워셜
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if ary[i][j] > ary[i][k] + ary[k][j]:
                ary[i][j] = ary[i][k] + ary[k][j]

# 주대각 성분을 기준으로 inf가 아닌 값의 대칭점에는 음수 값을 저장하기
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if ary[i][j] == INF:
            continue
        if ary[j][i] == INF:
            ary[j][i] = ary[i][j] * -1

s = int(sys.stdin.readline().rstrip())

for _ in range(s):
    a, b = map(int, sys.stdin.readline().split())
    if ary[a][b] == INF:
        print(0)
    elif ary[a][b] > 0:
        print(-1)
    elif ary[a][b] < 0:
        print(1)
