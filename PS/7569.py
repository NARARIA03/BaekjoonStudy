import sys
from collections import deque

# M : 가로 길이, N : 세로 길이, H :높이
M, N, H = map(int, sys.stdin.readline().split())


ary = [
    [list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)
]
queue = deque()


day = 0

# 처음 queue에 토마토가 심어진 z, y, x 좌표 enque
for z in range(H):
    for y in range(N):
        for x in range(M):
            if ary[z][y][x] == 1:
                queue.append((z, y, x))

while queue:
    day += 1
    length = len(queue)
    for _ in range(length):
        z, y, x = queue.popleft()

        z_max_flag = False
        z_min_flag = False
        x_max_flag = False
        x_min_flag = False
        y_max_flag = False
        y_min_flag = False

        if z == H - 1:
            z_max_flag = True
        if z == 0:
            z_min_flag = True

        if x == M - 1:
            x_max_flag = True
        if x == 0:
            x_min_flag = True

        if y == N - 1:
            y_max_flag = True
        if y == 0:
            y_min_flag = True

        if not z_max_flag and ary[z + 1][y][x] == 0:
            queue.append((z + 1, y, x))
            ary[z + 1][y][x] = 1
        if not z_min_flag and ary[z - 1][y][x] == 0:
            queue.append((z - 1, y, x))
            ary[z - 1][y][x] = 1
        if not x_max_flag and ary[z][y][x + 1] == 0:
            queue.append((z, y, x + 1))
            ary[z][y][x + 1] = 1
        if not x_min_flag and ary[z][y][x - 1] == 0:
            queue.append((z, y, x - 1))
            ary[z][y][x - 1] = 1
        if not y_max_flag and ary[z][y + 1][x] == 0:
            queue.append((z, y + 1, x))
            ary[z][y + 1][x] = 1
        if not y_min_flag and ary[z][y - 1][x] == 0:
            queue.append((z, y - 1, x))
            ary[z][y - 1][x] = 1

flag = True
for z in range(H):
    for y in range(N):
        for x in range(M):
            if ary[z][y][x] == 0:
                flag = False

if flag:
    print(day - 1)
else:
    print(-1)
