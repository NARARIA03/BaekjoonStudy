import sys
from collections import deque

# n : 세로, m : 가로
n, m = map(int, sys.stdin.readline().split())

dist = []
visited = [[0 for _ in range(m)] for _ in range(n)]

# 0 : 갈 수 없는 땅, 1 : 갈 수 있는 땅, 2 : 목적지
for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    dist.append(tmp)

queue = deque()
# 시작 지점 찾기
flag = False
for i in range(n):
    for j in range(m):
        if dist[i][j] == 2:
            start = (i, j)
            queue.append(start)  # 찾은 시작지점을 enque
            dist[i][j] = 0
            visited[i][j] = 1  # 방문 처리
            flag = True  # 2중 반복문 탈출을 위한 flag 변경
            break  # 내부 반복문 탈출
    if flag:  # 시작 지점 찾았으면
        break  # 외부 반복문도 탈출

cnt = 1
# BFS 구현 시작
while queue:
    # Phase 구분용 변수.각 Phase마다 몇 개의 땅이 enque 되었는지 세고, 그만큼만 돌린 뒤 cnt를 1 증가시킨다.
    length = len(queue)
    for _ in range(length):
        y, x = queue.popleft()

        # y가 top 아니면
        if y != 0:
            # y 위가 갈 수 있는 땅이고 방문하지 않았다면, 방문처리 하고 enque
            if dist[y - 1][x] == 1 and visited[y - 1][x] == 0:
                dist[y - 1][x] = cnt
                visited[y - 1][x] = 1
                queue.append((y - 1, x))

        # y가 bottom 아니면
        if y != n - 1:
            # y 아래가 갈 수 있는 땅이고 방문하지 않았다면, 방문처리 하고 enque
            if dist[y + 1][x] == 1 and visited[y + 1][x] == 0:
                dist[y + 1][x] = cnt
                visited[y + 1][x] = 1
                queue.append((y + 1, x))

        # x가 left 아니면
        if x != 0:
            # x 왼쪽이 갈 수 있는 땅이고 방문하지 않았다면, 방문처리 하고 enque
            if dist[y][x - 1] == 1 and visited[y][x - 1] == 0:
                dist[y][x - 1] = cnt
                visited[y][x - 1] = 1
                queue.append((y, x - 1))
        # x가 right 아니면
        if x != m - 1:
            # x 오른쪽이 갈 수 있는 땅이고 방문하지 않았다면, 방문처리 하고 enque
            if dist[y][x + 1] == 1 and visited[y][x + 1] == 0:
                dist[y][x + 1] = cnt
                visited[y][x + 1] = 1
                queue.append((y, x + 1))
    cnt += 1

# 원래 갈 수 있는 땅인 부분 중에서 도달할 수 없는 위치 구분해서 -1 처리
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and dist[i][j] == 1:
            dist[i][j] = -1

for i in range(n):
    for j in range(m):
        print(dist[i][j], end=" ")
    print()
