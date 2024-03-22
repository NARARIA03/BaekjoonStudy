import sys
from collections import deque

node_count = int(sys.stdin.readline())
vertex_count = int(sys.stdin.readline())

node = [[0 for _ in range(node_count + 1)] for _ in range(node_count + 1)]
visited = [0 for _ in range(node_count + 1)]

for _ in range(vertex_count):
    a, b = map(int, sys.stdin.readline().split())
    node[a][b] = 1
    node[b][a] = 1

queue = deque()
queue.append(1)
visited[1] = 1
virus_node = 0

while queue:
    v = queue.popleft()
    virus_node += 1

    for i in range(1, node_count + 1):
        if node[i][v] == 1 and visited[i] == 0:
            queue.append(i)
            visited[i] = 1
print(virus_node - 1)
