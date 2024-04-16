from sys import stdin, stdout

N, M = map(int, input().split())

ary = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    sum_value = 0
    l = list(map(int, input().split()))
    for j in range(1, N + 1):
        sum_value += l[j - 1]
        ary[i][j] = sum_value

for i in range(1, N):
    for j in range(1, N + 1):
        ary[i + 1][j] += ary[i][j]

# print("-------------------------")
# for row in ary:
#     print(*row)
res_ary = []
for _ in range(M):
    y1, x1, y2, x2 = map(int, input().split())
    # print(ary[y2][x2])
    # print(ary[y1 - 1][x2])
    # print(ary[y2][x1 - 1])
    # print(ary[y1 - 1][x1 - 1])
    res_ary.append(
        ary[y2][x2] - ary[y1 - 1][x2] - ary[y2][x1 - 1] + ary[y1 - 1][x1 - 1]
    )
    # print(ary[y2][x2] - ary[y1 - 1][x2] - ary[y2][x1 - 1] + ary[y1 - 1][x1 - 1])
for res in res_ary:
    print(res)
