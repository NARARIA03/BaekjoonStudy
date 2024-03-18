# 어느 회원이 다른 모든 회원과 친구이면, 이 회원의 점수는 1점이다.
# 어느 회원의 점수가 2점이면, 다른 모든 회원이 친구이거나 친구의 친구임을 말한다.
# 또한 어느 회원의 점수가 3점이면, 다른 모든 회원이 친구이거나, 친구의 친구이거나, 친구의 친구의 친구임을 말한다.
# -> 이 소리는, 모든 회원에 대한 회원 간 최소 간선의 길이를 구하고, 한 사람이 다른 사람들과 연결되는데 필요했던 최대 간선 길이가 점수라는 소리다!!

N = int(input())
INF = float("inf")
adj = [[INF for _ in range(N + 1)] for _ in range(N + 1)]

while 1:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    adj[a][b] = 1
    adj[b][a] = 1

# for row in adj:
#     print(*row)

# 플로이드 - 워셜 알고리즘을 돌려봅시다
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if adj[i][j] > adj[i][k] + adj[k][j]:
                adj[i][j] = adj[i][k] + adj[k][j]

for i in range(1, N + 1):
    adj[i][i] = 0

# for row in adj:
#     print(*row)

president = [INF]
for i in range(1, N + 1):
    max_value = -10000
    for j in range(1, N + 1):
        if max_value < adj[i][j]:
            max_value = adj[i][j]
    president.append(max_value)

# print(*president)
min_value = min(president)

print(min_value, president.count(min_value))
for i in range(1, N + 1):
    if president[i] == min_value:
        print(i, end=" ")

# 유명한 반례
# 2
# 1 2
# -1 -1

# 정답
# 1 2
# 1 2
# 내 코드 실행 결과
# 2 2
# 1 2

# 왜 그런지 로그를 통해 찾아보면...
# 처음 입력받은 인접행렬
# inf inf inf
# inf inf  1
# inf  1 inf

# 플로이드 - 워셜 돌리고 난 인접행렬
# inf inf inf
# inf 2 1
# inf 1 2

# 여기서 president 배열 상태
# inf 2 2

# 뮈가 문제인지 눈에 들어오는데, 주대각 성분 값이 2로 바껴버린게 문제다
# 주대각 성분을 다시 inf로 처리하고, 그 다음에 president 배열을 구해야겠다
# 주대각 성분을 inf 처리하니까, 실제 정답쪽에 inf가 나옴 -> 점수는 inf보다 작으면서 max인 값이니까!
# 따라서 주대각 성분을 0으로 처리했다.
