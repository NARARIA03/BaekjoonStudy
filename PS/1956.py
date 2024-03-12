V, E = map(int, input().split())
# 가중치 배열이자 인접행렬 역할을 하는 adj 배열 초기화
adj = [[float("inf") for _ in range(V + 1)] for _ in range(V + 1)]

for _ in range(E):
    # a -> b 경로에 대해 가중치가 다른 두 경로를 입력시키지는 않는다. 따라서 min()함수 쓸 필요는 X
    # adj[a][b]를 a -> b 라고 두도록 하겠다.
    a, b, c = map(int, input().split())
    adj[a][b] = c

# 플로이드 워셜 알고리즘으로 모든 정점에 대해 모든 정점까지의 최소경로를 구해보겠다.
for k in range(1, V + 1):
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            if adj[i][j] > adj[i][k] + adj[k][j]:
                adj[i][j] = adj[i][k] + adj[k][j]

# adj[0][0] 자리는 버리는 값임을 우리는 알고 있다.
# 어차피 경로 길이가 가장 짧은 사이클(제자리) 길이를 찾는 것이므로
# min값 초기화도 INF로 해야 되겠다 adj[0][0]에 min경로 길이를 저장하겠다
for i in range(1, V + 1):
    if adj[0][0] > adj[i][i]:
        adj[0][0] = adj[i][i]

# 만약 사이클(제자리) 경로가 존재하지 않는다면, 위 for문 실행 후에도 adj[0][0] = float("inf") 값일 것이다
# 경로가 존재하지 않으면 -1을 출력하라고 했다
if adj[0][0] == float("inf"):
    adj[0][0] = -1
print(adj[0][0])
