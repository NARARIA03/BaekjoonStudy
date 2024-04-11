import sys
from collections import deque

# [1] ~ [100] 까지 사용
board = [0 for _ in range(101)]
visited = [0 for _ in range(101)]
cur = 1
cnt = 0

# 사다리 수 N, 뱀의 수 M
N, M = map(int, sys.stdin.readline().split())

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    board[x] = y
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    board[u] = v

# BFS
queue = deque()
queue.append(cur)
visited[cur] = 1
is_finish = False

while queue:
    length = len(queue)
    for _ in range(length):
        cur = queue.popleft()
        if cur == 100:
            is_finish = True
            break
        # 뱀 또는 사다리 칸에 도착했다면
        elif board[cur] != 0:
            cur = board[cur]
            visited[cur] = 1

        # 주사위 던지고 진행
        if cur + 1 <= 100 and visited[cur + 1] == 0:
            visited[cur + 1] = 1
            queue.append(cur + 1)
        if cur + 2 <= 100 and visited[cur + 2] == 0:
            visited[cur + 2] = 1
            queue.append(cur + 2)
        if cur + 3 <= 100 and visited[cur + 3] == 0:
            visited[cur + 3] = 1
            queue.append(cur + 3)
        if cur + 4 <= 100 and visited[cur + 4] == 0:
            visited[cur + 4] = 1
            queue.append(cur + 4)
        if cur + 5 <= 100 and visited[cur + 5] == 0:
            visited[cur + 5] = 1
            queue.append(cur + 5)
        if cur + 6 <= 100 and visited[cur + 6] == 0:
            visited[cur + 6] = 1
            queue.append(cur + 6)
    # 100에 도달해서 반복문이 종료됬다면 탈출
    if is_finish:
        break
    # 아직 100에 도달하지 못했으면 주사위수 1 증가하고 다시 시작
    else:
        cnt += 1
# 정답 출력
print(cnt)
