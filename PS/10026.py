import sys
from collections import deque


def BFS_1(y, x):
    queue = deque()
    queue.append((y, x))
    color = color_ary[y][x]
    visited_1[y][x] = 1

    while queue:
        y, x = queue.popleft()
        if y != 0:
            if color_ary[y - 1][x] == color and visited_1[y - 1][x] == 0:
                visited_1[y - 1][x] = 1
                queue.append((y - 1, x))
        if y != N - 1:
            if color_ary[y + 1][x] == color and visited_1[y + 1][x] == 0:
                visited_1[y + 1][x] = 1
                queue.append((y + 1, x))

        if x != 0:
            if color_ary[y][x - 1] == color and visited_1[y][x - 1] == 0:
                visited_1[y][x - 1] = 1
                queue.append((y, x - 1))

        if x != N - 1:
            if color_ary[y][x + 1] == color and visited_1[y][x + 1] == 0:
                visited_1[y][x + 1] = 1
                queue.append((y, x + 1))


def BFS_2(y, x):
    queue = deque()
    queue.append((y, x))
    color = color_ary[y][x]
    visited_2[y][x] = 1

    if color == "R" or color == "G":
        while queue:
            y, x = queue.popleft()
            if y != 0:
                if (
                    color_ary[y - 1][x] == "R" or color_ary[y - 1][x] == "G"
                ) and visited_2[y - 1][x] == 0:
                    visited_2[y - 1][x] = 1
                    queue.append((y - 1, x))
            if y != N - 1:
                if (
                    color_ary[y + 1][x] == "R" or color_ary[y + 1][x] == "G"
                ) and visited_2[y + 1][x] == 0:
                    visited_2[y + 1][x] = 1
                    queue.append((y + 1, x))

            if x != 0:
                if (
                    color_ary[y][x - 1] == "R" or color_ary[y][x - 1] == "G"
                ) and visited_2[y][x - 1] == 0:
                    visited_2[y][x - 1] = 1
                    queue.append((y, x - 1))

            if x != N - 1:
                if (
                    color_ary[y][x + 1] == "R" or color_ary[y][x + 1] == "G"
                ) and visited_2[y][x + 1] == 0:
                    visited_2[y][x + 1] = 1
                    queue.append((y, x + 1))
    else:
        while queue:
            y, x = queue.popleft()
            if y != 0:
                if color_ary[y - 1][x] == color and visited_2[y - 1][x] == 0:
                    visited_2[y - 1][x] = 1
                    queue.append((y - 1, x))
            if y != N - 1:
                if color_ary[y + 1][x] == color and visited_2[y + 1][x] == 0:
                    visited_2[y + 1][x] = 1
                    queue.append((y + 1, x))

            if x != 0:
                if color_ary[y][x - 1] == color and visited_2[y][x - 1] == 0:
                    visited_2[y][x - 1] = 1
                    queue.append((y, x - 1))

            if x != N - 1:
                if color_ary[y][x + 1] == color and visited_2[y][x + 1] == 0:
                    visited_2[y][x + 1] = 1
                    queue.append((y, x + 1))


N = int(sys.stdin.readline().strip())

color_ary = []
# 적록색약 X 방문 처리 배열
visited_1 = [[0 for _ in range(N)] for _ in range(N)]
# 적록색약 방문 처리 배열
visited_2 = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(N):
    tmp = list(sys.stdin.readline().rstrip())
    color_ary.append(tmp)

count_1 = 0
count_2 = 0

for i in range(N):
    for j in range(N):
        if visited_1[i][j] == 0:
            BFS_1(i, j)
            count_1 += 1
        if visited_2[i][j] == 0:
            BFS_2(i, j)
            count_2 += 1
print(count_1, count_2)
