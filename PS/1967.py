from sys import stdin
import sys

sys.setrecursionlimit(10**4)


def DFS(start, adj, visited, sum_weight):
    visited[start] = 1
    flag = True
    for node, w in adj[start]:
        # print("node, w: ", node, w)
        if visited[node] == 0:
            flag = False
            DFS(node, adj, visited, sum_weight + w)
    if flag:
        global max_diameter
        global node_1
        if max_diameter < sum_weight:
            max_diameter = sum_weight
            node_1 = start
            # print("new diameter: ", max_diameter)


n = int(stdin.readline().rstrip())
max_diameter = 0
visited = [0 for _ in range(n + 1)]
adj = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    parent, child, weight = map(int, stdin.readline().split())
    adj[parent].append((child, weight))
    adj[child].append((parent, weight))


# for row in adj:
#     print(*row)


node_1 = 0

DFS(1, adj, visited, 0)
# print("어느 한 점으로부터 가장 먼 점:", node_1)
# 첫 DFS에서 쓰인 diameter값 초기화
max_diameter = 0
# 첫 DFS에서 쓰인 visited배열 초기화
for i in range(1, n + 1):
    visited[i] = 0
DFS(node_1, adj, visited, 0)

sys.stdout.write(str(max_diameter) + "\n")
