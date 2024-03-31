def DFS(start):
    visited[start] = 1

    for i in range(1, N + 1):
        if ary[start][i] == 1 and visited[i] == 0:
            DFS(i)


N, M = map(int, input().split())

ary = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    ary[a][b] = 1
    ary[b][a] = 1

visited = [0 for _ in range(N + 1)]

res = 0
for i in range(1, N + 1):
    if visited[i] == 0:
        DFS(i)
        res += 1
print(res)
