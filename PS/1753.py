import sys
import heapq

INF = float("inf")

# V = 정점 수, E = 간선 수
V, E = map(int, sys.stdin.readline().split())

# K = 시작 정점 번호
K = int(sys.stdin.readline().strip())

ary = [[] for _ in range(V + 1)]
dist = [INF for _ in range(V + 1)]

for _ in range(E):
    # ary[u] = (w, v) 라면, u -> v 의 가중치가 w라는 뜻이라고 약속.
    u, v, w = map(int, sys.stdin.readline().split())
    # 아래 flag는 ary[u]에 이미 v와 연결된 간선 정보가 존재하는지 확인하기 위해 사용
    flag = True
    # 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다라고 문제에 나와있다.
    for i in range(len(ary[u])):
        # ary[u]에 저장된 값을 하나씩 뽑는다. j는 가중치, k는 도착노드이다.
        j, k = ary[u][i]
        # u -> v가 이미 있는 경로라면 flag를 false로 바꾸고, 가중치를 비교한다
        if k == v:
            flag = False
            # 새로 입력으로 들어온 가중치가 더 작다면, 새 가중치로 교체
            if j > w:
                ary[u][i] = (w, v)
    # 한 번도 들어온 적 없는 경로라면 append로 배열에 추가
    if flag:
        ary[u].append((w, v))

# 시작 정점 위치를 최소heap에 삽입
heap = []
# 위치는 K이고, 가중치는 0이라는 의미의 데이터를 heap에 삽입
heapq.heappush(heap, (0, K))
# K의 거리 0으로 세팅
dist[K] = 0
while heap:
    # heap에서 가중치랑 도착노드 정보를 뽑는다
    w, v = heapq.heappop(heap)
    # 도착노드에서 출발해 갈 수 있는 노드들을 반복문으로 하나씩 체크한다
    for node in ary[v]:
        w2, v2 = node
        # 도착 노드에서 출발해서 갈 수 있는 노드들 중
        # 우리의 시작 노드에서 도착 노드를 경유해 가는 경우의 총 가중치가 더 작다면 -> 갱신
        if dist[v2] > w + w2:
            dist[v2] = w + w2
            # heap에 갱신된 가중치로 다시 push
            heapq.heappush(heap, (w + w2, v2))

for i in range(1, V + 1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])
