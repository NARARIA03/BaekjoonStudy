# n = 도시의 수 (2 이상 100 이하) -> 노드
# m = 버스의 수 (1 이상 100000 이하) -> 간선
# 문제를 읽어보니, 단방향 가중치 그래프인것 같다

n = int(input())
m = int(input())

# distance 배열 생성
dist = [[float("inf") for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    # a = 시작 도시, b = 도착 도시, c = 버스 가격
    a, b, c = map(int, input().split())
    # 문제 본문 : 시작 도시와 도착 도시를 연결하는 노선(버스)는 하나가 아니다. -> 입력에서 1, 1, 1과 1, 1, 100000이 들어올 수 있다.
    # dist에 가중치를 매길 때 min으로 최소값을 가져가도록 구현하지 않는다면, 100000의 가중치를 써버리게 된다. 그러지 않기 위해 min으로 최소값을 가지도록 해준다.
    dist[a][b] = min(dist[a][b], c)  # 가중치 배열에 가격 저장.


# 가중치 방향 그래프에 대한 플로이드 워셜 알고리즘 작성
# 플로이드 워셜 알고리즘으로 모든 정점에 대해, 모든 정점까지의 거리 계산
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

# 플로이드 워셜 알고리즘 종료된 dist 배열 전처리 (inf 값은 0으로 변경, [i][i]에 해당하는 것들 0으로 변경)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dist[i][j] == float("inf"):
            dist[i][j] = 0
        elif i == j:
            dist[i][j] = 0

# 전처리한 배열 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(dist[i][j], end=" ")
    print()
