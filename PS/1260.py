# N : 정점의 개수
# M : 간선의 개수
# V : 시작 정점번호
N, M, V = map(int, input().split())

# N + 1 by N + 1 짜리 인접 행렬 생성, [0][0]은 무시하고, 1과 2가 서로 연결된 정점이라면 [1][2] == [2][1] == 1, 연결되지 않았다면 0이다.
graph = [[0 for _ in range(0, N + 1)] for _ in range(0, N + 1)]

for i in range(M):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1

visited_DFS = [0 for _ in range(N + 1)]
visited_BFS = [0 for _ in range(N + 1)]

def DFS (V):
    # 시작 노드 방문 처리
    visited_DFS[V] = 1
    print(V, end=" ")
    for i in range(1, N + 1):
        if (graph[V][i] == 1 and graph[i][V] == 1 and visited_DFS[i] == 0):
            DFS(i)

def BFS (V):
    # 시작 노드 방문 처리
    visited_BFS[V] = 1
    # 큐에 시작노드 추가
    queue = [V]
    while (queue):
        V = queue.pop(0)
        print(V, end= " ")
        visited_BFS[V] = 1
        for i in range(1, N + 1):
            if (graph[V][i] == 1 and graph[i][V] == 1 and visited_BFS[i] == 0 and i not in queue):
                queue.append(i)

DFS(V)
print()
BFS(V)