# N = 학생 수, M = 두 학생 키를 비교한 횟수 (반복문에 사용)
N, M = map(int, input().split())

# 생각해보니까 인접행렬 등을 만들지 않고, dist 2차원 배열 자체를 인접 행렬로 활용이 가능하다.
dist = [[float("inf") for _ in range(N + 1)] for _ in range(N + 1)]

# M번의 두 학생 키 비교를 수행해서 dist[a][b]에 1을 집어넣는다. 이는 a보다 b가 더 큼을 의미한다.
for _ in range(M):
    a, b = map(int, input().split())
    dist[a][b] = 1

# 플로이드 워셜 알고리즘을 사용해 모든 학생에 대해 키를 비교할 수 있다면, 모두 비교한다.
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

# dist 배열의 값은 간선 길이거나, INF 상태일 것이다.
# 만약 INF라면 0으로 처리하고, 간선 길이(키 비교 가능)라면 1로 처리한다.
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if dist[i][j] == float("inf"):
            dist[i][j] = 0
        else:
            dist[i][j] = 1

# 질문 게시판을 통해 얻은 아이디어
# 한 학생이 다른 모든 학생에 대해 키가 크거나 작음을 파악 가능하다면 -> cnt += 1 하면 된다.
# [1][2]가 1이거나, [2][1]이 1이라면, 1과 2의 키 크기는 비교가 된 것이다.
# 즉 본인을 제외하고, 다른 모든 학생들에 대해 [본인][다른학생] = 1 이거나, [다른학생][본인] = 1 이라면, 본인의 키가 몇 번째인지 알 수 있다고 볼 수 있다.
cnt = 0
for i in range(1, N + 1):
    flag = True
    for j in range(1, N + 1):
        if i == j:
            continue
        elif dist[i][j] == 1 or dist[j][i] == 1:
            continue
        else:
            flag = False
    if flag:
        cnt += 1
print(cnt)
