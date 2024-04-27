from itertools import combinations
from collections import deque
from copy import deepcopy


# maps 배열에서 0이 담긴 좌표들이 담긴 배열 반환
def find_blank_idx_ary(maps: list):
    idx_ary = []
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 0:
                idx_ary.append((i, j))
    return idx_ary


# maps 배열에서 벽 3개를 세울 수 있는 모든 경우의 수에 대한 좌표 묶음 배열 반환
def find_new_wall_combination(blank_idx_ary: list):
    blank_combination = list(combinations(blank_idx_ary, 3))
    # print(len(blank_combination))
    return blank_combination


# maps 배열에서 바이러스의 좌표들이 담긴 배열 반환
def find_virus_idx_ary(maps: list):
    idx_ary = []
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 2:
                idx_ary.append((i, j))
    return idx_ary


# find_new_wall_combination()로 받은 하나의 좌표 묶음에 대해 벽을 친 새 maps를 반환
def make_new_wall_map(maps: list, blank_set: set):
    copy_maps = deepcopy(maps)
    for wall in blank_set:
        y, x = wall
        copy_maps[y][x] = 1
    return copy_maps


# BFS를 돌려 바이러스를 퍼뜨림
def BFS(maps: list, visited: list):
    queue = deque()
    for virus in virus_idx_ary:
        queue.append(virus)

    while queue:
        y, x = queue.popleft()
        if y != 0:
            if maps[y - 1][x] == 0 and visited[y - 1][x] == 0:
                maps[y - 1][x] = 1
                visited[y - 1][x] = 1
                queue.append((y - 1, x))
        if y != N - 1:
            if maps[y + 1][x] == 0 and visited[y + 1][x] == 0:
                maps[y + 1][x] = 1
                visited[y + 1][x] = 1
                queue.append((y + 1, x))
        if x != 0:
            if maps[y][x - 1] == 0 and visited[y][x - 1] == 0:
                maps[y][x - 1] = 1
                visited[y][x - 1] = 1
                queue.append((y, x - 1))
        if x != M - 1:
            if maps[y][x + 1] == 0 and visited[y][x + 1] == 0:
                maps[y][x + 1] = 1
                visited[y][x + 1] = 1
                queue.append((y, x + 1))
    return maps


# BFS가 끝난 maps 배열에 대해 0의 개수를 세서 반환
def count_safe_area(maps: list):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 0:
                cnt += 1
    return cnt


# 0: 빈칸
# 1: 벽
# 2: 바이러스
# N: 세로
# M: 가로
N, M = map(int, input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))

# 연구소 내 비어있는 곳의 (y, x) 인덱스 쌍을 반환받음
blank_idx_ary = find_blank_idx_ary(maps)

# 연구소 내 바이러스의 (y, x) 인덱스 쌍을 반환받음
virus_idx_ary = find_virus_idx_ary(maps)

# 연구소 내 비어있는 곳 중 3군데에 벽을 추가로 만드는 모든 경우의 수를 반환받음
# ((y1, x1), (y2, x2), (y3, x3)) 형식임
wall_combination_ary = find_new_wall_combination(blank_idx_ary)

safe_area_size = 0
# 벽 3개를 추가로 치는 모든 경우에 대해
for blank_set in wall_combination_ary:
    # 방문 처리 배열
    visited = [[0 for _ in range(M)] for _ in range(N)]
    # 벽 3개를 친 새로운 배열
    c_maps = make_new_wall_map(maps, blank_set)
    # 벽 3개를 친 배열로 BFS 수행
    finish_bfs_maps = BFS(c_maps, visited)
    # BFS 결과 0의 개수를 구함
    cnt = count_safe_area(finish_bfs_maps)
    # BFS 결과 0의 개수가 safe_area_size보다 크면 업데이트
    if safe_area_size < cnt:
        safe_area_size = cnt

print(safe_area_size)
