import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

INF = float("inf")
adj = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

route = [[[] for i in range(n + 1)] for j in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    # a -> b 가는데 비용이 가장 작은 값을 채택하도록 if문
    if c < adj[a][b]:
        adj[a][b] = c
        route[a][b] = [a, b]

# 플로이드 워셜 사용
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if adj[i][j] > adj[i][k] + adj[k][j]:
                adj[i][j] = adj[i][k] + adj[k][j]
                # 경로를 i -> k -> j로 가도록 업데이트
                route[i][j] = list(route[i][k]) + list(route[k][j])

# 대각 행렬 부분 0으로 초기화
for i in range(1, n + 1):
    adj[i][i] = 0
    route[i][i] = []

# 현재 route를 print 찍어보면, k 부분 또는 j 부분이 중복된다. ([1, 3, 5]의 경우 -> [1, 3, 3, 5]와 같이 저장되어 있음)
# route를 순회 돌며 중복 체크용 set을 활용해 중복 부분을 제거한 최종 배열 res_ary를 생성
res_ary = []
for i in range(1, n + 1):
    for j in range(1, n + 1):
        unique_route = []
        seen = set()
        for x in route[i][j]:
            if x not in seen:
                unique_route.append(x)
                seen.add(x)
        res_ary.append(list(unique_route))

# i -> j로 가는데 필요한 최소 비용 출력하는 부분, 못 가는 경우 0으로 출력해야 함에 주의해야 한다
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if adj[i][j] == INF:
            print(0, end=" ")
            continue
        print(adj[i][j], end=" ")
    print()

# i -> j로 가는데 거치는 도시의 수와, 경로를 출력하는 부분이다.
for i in range(len(res_ary)):
    print(len(res_ary[i]), end=" ")
    print(*res_ary[i])
