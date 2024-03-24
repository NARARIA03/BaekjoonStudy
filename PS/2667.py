from collections import deque


def BFS(start_y, start_x):
    queue = deque()
    queue.append((start_y, start_x))
    # 방문 처리는 queue에 추가할 때 해야 탈이 없다 (중복 enque 발생 안함)
    apt[start_y][start_x] = 0
    cnt = 0

    while queue:
        y, x = queue.popleft()
        cnt += 1

        # y가 0이 아니면 배열 위쪽 원소 접근
        if y != 0:
            if apt[y - 1][x] == 1:
                queue.append((y - 1, x))
                # 방문 처리는 queue에 추가할 때 해야 탈이 없다 (중복 enque 발생 안함)
                apt[y - 1][x] = 0

        # y가 length - 1이 아니면 배열 아래쪽 원소 접근
        if y != len(apt) - 1:
            if apt[y + 1][x] == 1:
                queue.append((y + 1, x))
                # 방문 처리는 queue에 추가할 때 해야 탈이 없다 (중복 enque 발생 안함)
                apt[y + 1][x] = 0

        # x가 0이 아니면 배열 왼쪽 원소 접근
        if x != 0:
            if apt[y][x - 1] == 1:
                queue.append((y, x - 1))
                # 방문 처리는 queue에 추가할 때 해야 탈이 없다 (중복 enque 발생 안함)
                apt[y][x - 1] = 0

        # x가 length - 1이 아니면 배열 오른쪽 원소 접근
        if x != len(apt[0]) - 1:
            if apt[y][x + 1] == 1:
                queue.append((y, x + 1))
                # 방문 처리는 queue에 추가할 때 해야 탈이 없다 (중복 enque 발생 안함)
                apt[y][x + 1] = 0
    return cnt


N = int(input())
apt = []
for _ in range(N):
    tmp = input()
    tmp_list = []
    for char in tmp:
        tmp_list.append(int(char))
    apt.append(tmp_list)

dnaji_cnt = 0
res_ary = []

for i in range(N):
    for j in range(N):
        if apt[i][j] == 1:
            dnaji_cnt += 1
            res_ary.append(BFS(i, j))
res_ary.sort()
print(dnaji_cnt)
for res in res_ary:
    print(res)
