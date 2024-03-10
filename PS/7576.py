import sys
from collections import deque


# 토마토가 전부 익어야만 True를 반환하는 함수. -1은 무시한다
def check_tomato(tomato):
    for row in tomato:
        for item in row:
            if item == 0:
                return False
            else:
                continue
    return True


# 2 ≤ M,N ≤ 1,000
# M : 가로 길이, N : 세로 길이
M, N = map(int, sys.stdin.readline().split())
tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# BFS 시 사용될 visited 배열
visited = [[0 for _ in range(M)] for _ in range(N)]

# 날짜 값
day = 0

# BFS에 사용할 queue를 선언하고, 초기 1 (익은 토마토) 좌표를 큐에 enque 수행
queue = deque()
for y in range(N):
    for x in range(M):
        if tomato[y][x] == 1:
            queue.append([x, y])
            visited[y][x] = 1  # x, y 좌표 방문 처리 (큐에 넣을 때 방문처리하자)

while queue:
    # 모든 토마토가 익었다면 반복문 종료
    flag = check_tomato(tomato)
    if flag:
        break
    # 각 날짜별로 큐에서 빼야 할 개수가 정해져있다. 예를들어 init 익은토마토가 2개라면
    # while문 밖에서 enque 수행을 두 번 했을 것이고, len(queue) == 2 일 것이다.
    # 별다른 빈 토마토가 없다고 생각하고, 두 익은 토마토가 우상단, 좌상단에 있다고 치면
    # 첫째 날 deque 해서 처리해야 하는 토마토는 2개 -> queue에 4개의 토마토 좌표가 enque
    # 둘째 날 deque 해서 처리해야 하는 토마토는 4개 (각 꼭지점에서는 최대 두 개의 토마토를 익게 할 수 있음) -> queue에 6개의 토마토 좌표가 enque
    # 넷째 날 deque 해서 처리해야 하는 토마토는 6개 ... 반복\
    length = len(queue)

    for _ in range(length):
        x, y = queue.popleft()
        # x, y 좌표에 따라 index out of range 되지 않도록 조건문 사용
        # 꼭짓점 4군데에 대한 조건
        # 좌상단
        if x == 0 and y == 0:
            # 오른쪽 토마토가 존재하고, 방문처리되지 않았다면
            if tomato[y][x + 1] == 0 and visited[y][x + 1] == 0:
                tomato[y][x + 1] = 1  # 익음 처리
                queue.append([x + 1, y])  # enque
                visited[y][x + 1] = 1  # 방문 처리
            # 아래 토마토가 존재하고, 방문처리되지 않았다면
            if tomato[y + 1][x] == 0 and visited[y + 1][x] == 0:
                tomato[y + 1][x] = 1  # 익음 처리
                queue.append([x, y + 1])  # enque
                visited[y + 1][x] = 1  # 방문 처리
        # 좌하단
        elif x == 0 and y == N - 1:
            # 위쪽 토마토가 존재하고, 방문처리되지 않았다면
            if tomato[y - 1][x] == 0 and visited[y - 1][x] == 0:
                tomato[y - 1][x] = 1  # 익음 처리
                queue.append([x, y - 1])  # enque
                visited[y - 1][x] = 1  # 방문 처리
            # 오른쪽 토마토가 존재하고, 방문처리되지 않았다면
            if tomato[y][x + 1] == 0 and visited[y][x + 1] == 0:
                tomato[y][x + 1] = 1  # 익음 처리
                queue.append([x + 1, y])  # enque
                visited[y][x + 1] = 1  # 방문 처리
        # 우상단
        elif x == M - 1 and y == 0:
            # 왼쪽 토마토가 존재하고, 방문처리되지 않았다면
            if tomato[y][x - 1] == 0 and visited[y][x - 1] == 0:
                tomato[y][x - 1] = 1  # 익음 처리
                queue.append([x - 1, y])  # enque
                visited[y][x - 1] = 1  # 방문 처리
            # 아래 토마토가 존재하고, 방문처리되지 않았다면
            if tomato[y + 1][x] == 0 and visited[y + 1][x] == 0:
                tomato[y + 1][x] = 1  # 익음 처리
                queue.append([x, y + 1])  # enque
                visited[y + 1][x] = 1  # 방문 처리
        # 우하단
        elif x == M - 1 and y == N - 1:
            # 위쪽 토마토가 존재하고, 방문처리되지 않았다면
            if tomato[y - 1][x] == 0 and visited[y - 1][x] == 0:
                tomato[y - 1][x] = 1  # 익음 처리
                queue.append([x, y - 1])  # enque
                visited[y - 1][x] = 1  # 방문 처리
            # 왼쪽 토마토가 존재하고, 방문처리되지 않았다면
            if tomato[y][x - 1] == 0 and visited[y][x - 1] == 0:
                tomato[y][x - 1] = 1  # 익음 처리
                queue.append([x - 1, y])  # enque
                visited[y][x - 1] = 1  # 방문 처리
        # 상단
        elif y == 0:
            # 왼쪽 토마토가 존재하고, 방문처리되지 않았다면
            if tomato[y][x - 1] == 0 and visited[y][x - 1] == 0:
                tomato[y][x - 1] = 1  # 익음 처리
                queue.append([x - 1, y])  # enque
                visited[y][x - 1] = 1  # 방문 처리
            # 오른쪽 토마토가 존재하고, 방문처리되지 않았다면
            if tomato[y][x + 1] == 0 and visited[y][x + 1] == 0:
                tomato[y][x + 1] = 1  # 익음 처리
                queue.append([x + 1, y])  # enque
                visited[y][x + 1] = 1  # 방문 처리
            # 아래 토마토가 존재하고, 방문처리되지 않았다면
            if tomato[y + 1][x] == 0 and visited[y + 1][x] == 0:
                tomato[y + 1][x] = 1  # 익음 처리
                queue.append([x, y + 1])  # enque
                visited[y + 1][x] = 1  # 방문 처리
        # 하단
        elif y == N - 1:
            # 왼쪽 토마토가 존재하고, 방문처리되지 않았다면
            if tomato[y][x - 1] == 0 and visited[y][x - 1] == 0:
                tomato[y][x - 1] = 1  # 익음 처리
                queue.append([x - 1, y])  # enque
                visited[y][x - 1] = 1  # 방문 처리
            # 오른쪽 토마토가 존재하고, 방문처리되지 않았다면
            if tomato[y][x + 1] == 0 and visited[y][x + 1] == 0:
                tomato[y][x + 1] = 1  # 익음 처리
                queue.append([x + 1, y])  # enque
                visited[y][x + 1] = 1  # 방문 처리
            # 위쪽 토마토가 존재하고, 방문처리되지 않았다면
            if tomato[y - 1][x] == 0 and visited[y - 1][x] == 0:
                tomato[y - 1][x] = 1  # 익음 처리
                queue.append([x, y - 1])  # enque
                visited[y - 1][x] = 1  # 방문 처리
        # 왼쪽
        elif x == 0:
            # 위쪽 토마토가 존재하고, 방문처리되지 않았다면
            if tomato[y - 1][x] == 0 and visited[y - 1][x] == 0:
                tomato[y - 1][x] = 1  # 익음 처리
                queue.append([x, y - 1])  # enque
                visited[y - 1][x] = 1  # 방문 처리
            # 아래 토마토가 존재하고, 방문처리되지 않았다면
            if tomato[y + 1][x] == 0 and visited[y + 1][x] == 0:
                tomato[y + 1][x] = 1  # 익음 처리
                queue.append([x, y + 1])  # enque
                visited[y + 1][x] = 1  # 방문 처리
            # 오른쪽 토마토가 존재하고, 방문처리되지 않았다면
            if tomato[y][x + 1] == 0 and visited[y][x + 1] == 0:
                tomato[y][x + 1] = 1  # 익음 처리
                queue.append([x + 1, y])  # enque
                visited[y][x + 1] = 1  # 방문 처리
        # 오른쪽
        elif x == M - 1:
            # 왼쪽 토마토가 존재하고, 방문처리되지 않았다면
            if tomato[y][x - 1] == 0 and visited[y][x - 1] == 0:
                tomato[y][x - 1] = 1  # 익음 처리
                queue.append([x - 1, y])  # enque
                visited[y][x - 1] = 1  # 방문 처리
            # 위쪽 토마토가 존재하고, 방문처리되지 않았다면
            if tomato[y - 1][x] == 0 and visited[y - 1][x] == 0:
                tomato[y - 1][x] = 1  # 익음 처리
                queue.append([x, y - 1])  # enque
                visited[y - 1][x] = 1  # 방문 처리
            # 아래 토마토가 존재하고, 방문처리되지 않았다면
            if tomato[y + 1][x] == 0 and visited[y + 1][x] == 0:
                tomato[y + 1][x] = 1  # 익음 처리
                queue.append([x, y + 1])  # enque
                visited[y + 1][x] = 1  # 방문 처리
        # 중간어딘가
        else:
            # 위쪽 토마토가 존재하고, 방문처리되지 않았다면
            if tomato[y - 1][x] == 0 and visited[y - 1][x] == 0:
                tomato[y - 1][x] = 1  # 익음 처리
                queue.append([x, y - 1])  # enque
                visited[y - 1][x] = 1  # 방문 처리
            # 아래 토마토가 존재하고, 방문처리되지 않았다면
            if tomato[y + 1][x] == 0 and visited[y + 1][x] == 0:
                tomato[y + 1][x] = 1  # 익음 처리
                queue.append([x, y + 1])  # enque
                visited[y + 1][x] = 1  # 방문 처리
            # 왼쪽 토마토가 존재하고, 방문처리되지 않았다면
            if tomato[y][x - 1] == 0 and visited[y][x - 1] == 0:
                tomato[y][x - 1] = 1  # 익음 처리
                queue.append([x - 1, y])  # enque
                visited[y][x - 1] = 1  # 방문 처리
            # 오른쪽 토마토가 존재하고, 방문처리되지 않았다면
            if tomato[y][x + 1] == 0 and visited[y][x + 1] == 0:
                tomato[y][x + 1] = 1  # 익음 처리
                queue.append([x + 1, y])  # enque
                visited[y][x + 1] = 1  # 방문 처리
    day += 1

# 큐가 비면, while문이 종료된다.
# 따라서, while문이 종료되면, 현재 토마토리스트가 모두 익었는지 안 익었는지 확인하고, 이에 맞게 반환한다.
res_flag = check_tomato(tomato)
if res_flag:
    print(day)
else:
    print(-1)
