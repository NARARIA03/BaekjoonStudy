import sys


INF = float("inf")

N = int(sys.stdin.readline().strip())

adj = [[INF for _ in range(N + 1)] for _ in range(N + 1)]

M = int(sys.stdin.readline().strip())

for _ in range(M):
    # a, b 입력 -> 무게 : a > b -> 단방향 그래프
    # 무게 크기 비교만 하면 되므로 가중치는 X
    a, b = map(int, sys.stdin.readline().split())

    # [a][b] == a > b 를 의미한다고 약속
    adj[a][b] = 1

for i in range(1, N + 1):
    adj[i][i] = 0
# 플로이드 워셜로 모든 노드에 대해 모든 노드까지 이동하는데 필요한 최소 거리를 구함
# <- 거리값이 INF가 아니라면 무게 비교가 가능하다는 뜻이 된다.
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if adj[i][j] > adj[i][k] + adj[k][j]:
                adj[i][j] = adj[i][k] + adj[k][j]

# 아래 이중 for문은 이런 케이스를 막기 위해 추가하였다.
# 플로이드 워셜만 돌리고 나서 INF를 세어보니 정답과 너무 달랐다.
# 왜냐면 어떤 값보다 "크다" 라는 개념으로 크기 비교가 가능한 Case만 날렸기 때문이다.

# 1 2 입력이 들어왔으면 1 > 2 라는 의미이고, [1][2] = 1로 지정했으나, 사실 [2][1]도 크기는 비교가 가능한 것이다.
# 왜냐면 2가 1보다 작다! 라는 비교가 가능하기 때문이다.
# 따라서 하나의 입력으로 두 개의 크기 비교 정보가 들어온다는 뜻이다.

# 그렇다고 해서 양방향 그래프로 만들면 안된다.
# 문제 조건을 보면 비교 결과가 모순되는 입력은 없다는 메시지가 있다 <- 이게 양방향으로 넣지 말라는 의미이다.

# 그럼 어떻게 해야 하는가? -> [a][b] 가 최종적으로 플로이드 워셜을 돌렸더니 크기 비교가 a > b로서 가능했다면
# [b][a]도 크기 비교가 가능하다는 사실만 남겨주는 것이다.
# 주대각 성분을 기준으로 대칭되는 두 값중 하나만 INF 라면, 이 INF도 숫자로 그냥 바꿔버리는 것이다!

# 그렇게 하면, 어떤 값보다 "작다" 라는 개념으로 크기 비교가 가능한 Case가 날아가면서 각 행의 INF 개수가 정답과 같아진다
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if adj[i][j] != INF and adj[j][i] == INF:
            adj[j][i] = adj[i][j]

for i in range(1, N + 1):
    cnt = 0
    for j in range(1, N + 1):
        if adj[i][j] == INF:
            cnt += 1
    sys.stdout.write(str(cnt) + "\n")
