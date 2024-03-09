import sys
from collections import deque


def BFS(graph, visited, M, N, x, y):
    queue = deque()
    queue.append([x, y])
    while queue:
        this_x, this_y = queue.popleft()
        visited[this_y][this_x] = 1
        graph[this_y][this_x] = 0

        if this_y == 0 and this_x == 0:
            if graph[this_y][this_x + 1] == 1 and visited[this_y][this_x + 1] == 0:
                queue.append([this_x + 1, this_y])
                visited[this_y][this_x + 1] = 1
            if graph[this_y + 1][this_x] == 1 and visited[this_y + 1][this_x] == 0:
                queue.append([this_x, this_y + 1])
                visited[this_y + 1][this_x] = 1

        elif this_y == 0 and this_x == M - 1:
            if graph[this_y][this_x - 1] == 1 and visited[this_y][this_x - 1] == 0:
                queue.append([this_x - 1, this_y])
                visited[this_y][this_x - 1] = 1
            if graph[this_y + 1][this_x] == 1 and visited[this_y + 1][this_x] == 0:
                queue.append([this_x, this_y + 1])
                visited[this_y + 1][this_x] = 1

        elif this_y == N - 1 and this_x == 0:
            if graph[this_y - 1][this_x] == 1 and visited[this_y - 1][this_x] == 0:
                queue.append([this_x, this_y - 1])
                visited[this_y - 1][this_x] = 1
            if graph[this_y][this_x + 1] == 1 and visited[this_y][this_x + 1] == 0:
                queue.append([this_x + 1, this_y])
                visited[this_y][this_x + 1] = 1

        elif this_y == N - 1 and this_x == M - 1:
            if graph[this_y][this_x - 1] == 1 and visited[this_y][this_x - 1] == 0:
                queue.append([this_x - 1, this_y])
                visited[this_y][this_x - 1] = 1
            if graph[this_y - 1][this_x] == 1 and visited[this_y - 1][this_x] == 0:
                queue.append([this_x, this_y - 1])
                visited[this_y - 1][this_x] = 1

        elif this_y == 0:
            if graph[this_y][this_x - 1] == 1 and visited[this_y][this_x - 1] == 0:
                queue.append([this_x - 1, this_y])
                visited[this_y][this_x - 1] = 1
            if graph[this_y + 1][this_x] == 1 and visited[this_y + 1][this_x] == 0:
                queue.append([this_x, this_y + 1])
                visited[this_y + 1][this_x] = 1
            if graph[this_y][this_x + 1] == 1 and visited[this_y][this_x + 1] == 0:
                queue.append([this_x + 1, this_y])
                visited[this_y][this_x + 1] = 1

        elif this_x == 0:
            if graph[this_y - 1][this_x] == 1 and visited[this_y - 1][this_x] == 0:
                queue.append([this_x, this_y - 1])
                visited[this_y - 1][this_x] = 1
            if graph[this_y + 1][this_x] == 1 and visited[this_y + 1][this_x] == 0:
                queue.append([this_x, this_y + 1])
                visited[this_y + 1][this_x] = 1
            if graph[this_y][this_x + 1] == 1 and visited[this_y][this_x + 1] == 0:
                queue.append([this_x + 1, this_y])
                visited[this_y][this_x + 1] = 1

        elif this_y == N - 1:
            if graph[this_y][this_x - 1] == 1 and visited[this_y][this_x - 1] == 0:
                queue.append([this_x - 1, this_y])
                visited[this_y][this_x - 1] = 1
            if graph[this_y][this_x + 1] == 1 and visited[this_y][this_x + 1] == 0:
                queue.append([this_x + 1, this_y])
                visited[this_y][this_x + 1] = 1
            if graph[this_y - 1][this_x] == 1 and visited[this_y - 1][this_x] == 0:
                queue.append([this_x, this_y - 1])
                visited[this_y - 1][this_x] = 1

        elif this_x == M - 1:
            if graph[this_y][this_x - 1] == 1 and visited[this_y][this_x - 1] == 0:
                queue.append([this_x - 1, this_y])
                visited[this_y][this_x - 1] = 1
            if graph[this_y + 1][this_x] == 1 and visited[this_y + 1][this_x] == 0:
                queue.append([this_x, this_y + 1])
                visited[this_y + 1][this_x] = 1
            if graph[this_y - 1][this_x] == 1 and visited[this_y - 1][this_x] == 0:
                queue.append([this_x, this_y - 1])
                visited[this_y - 1][this_x] = 1
        else:
            if graph[this_y][this_x - 1] == 1 and visited[this_y][this_x - 1] == 0:
                queue.append([this_x - 1, this_y])
                visited[this_y][this_x - 1] = 1
            if graph[this_y][this_x + 1] == 1 and visited[this_y][this_x + 1] == 0:
                queue.append([this_x + 1, this_y])
                visited[this_y][this_x + 1] = 1
            if graph[this_y + 1][this_x] == 1 and visited[this_y + 1][this_x] == 0:
                queue.append([this_x, this_y + 1])
                visited[this_y + 1][this_x] = 1
            if graph[this_y - 1][this_x] == 1 and visited[this_y - 1][this_x] == 0:
                queue.append([this_x, this_y - 1])
                visited[this_y - 1][this_x] = 1


T = int(sys.stdin.readline())

for _ in range(T):
    # 배추밭 가로 길이 M
    # 배추밭 세로 길이 N
    # 배추의 위치 개수 K
    M, N, K = map(int, sys.stdin.readline().split())

    cabbage_list = [[0 for _ in range(M)] for _ in range(N)]
    visited_list = [[0 for _ in range(M)] for _ in range(N)]
    cnt = 0

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        cabbage_list[y][x] = 1

    for y in range(N):
        for x in range(M):
            if visited_list[y][x] == 1:
                continue
            elif cabbage_list[y][x] == 0:
                visited_list[y][x] = 1
                continue
            elif cabbage_list[y][x] == 1:
                visited_list[y][x] = 1
                cnt += 1
                BFS(cabbage_list, visited_list, M, N, x, y)

    sys.stdout.write(str(cnt) + "\n")

# BFS를 큐로 구현하게 되면, 반드시 visited 배열이 필요하다!!
# 아래 글 참고
# https://djm03178.tistory.com/31
