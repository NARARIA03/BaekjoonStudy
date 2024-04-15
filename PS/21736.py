from collections import deque

N, M = map(int, input().split())

campus = []
visited = [[0 for _ in range(M)] for _ in range(N)]
people_count = 0
queue = deque()

for _ in range(N):
    tmp = list(input())
    campus.append(tmp)

search_I_flag = False
for i in range(N):
    if search_I_flag:
        break
    for j in range(M):
        if campus[i][j] == "I":
            queue.append((i, j))  # 큐에 도연이 위치 저장
            visited[i][j] = 1  # 도연이 위치 방문처리
            search_I_flag = True
            break

while queue:
    y, x = queue.popleft()
    if y != 0 and visited[y - 1][x] == 0:
        if campus[y - 1][x] == "O":
            queue.append((y - 1, x))
            visited[y - 1][x] = 1

        elif campus[y - 1][x] == "P":
            people_count += 1
            queue.append((y - 1, x))
            visited[y - 1][x] = 1

    if y != N - 1 and visited[y + 1][x] == 0:
        if campus[y + 1][x] == "O":
            queue.append((y + 1, x))
            visited[y + 1][x] = 1

        elif campus[y + 1][x] == "P":
            people_count += 1
            queue.append((y + 1, x))
            visited[y + 1][x] = 1

    if x != 0 and visited[y][x - 1] == 0:
        if campus[y][x - 1] == "O":
            queue.append((y, x - 1))
            visited[y][x - 1] = 1

        elif campus[y][x - 1] == "P":
            people_count += 1
            queue.append((y, x - 1))
            visited[y][x - 1] = 1

    if x != M - 1 and visited[y][x + 1] == 0:
        if campus[y][x + 1] == "O":
            queue.append((y, x + 1))
            visited[y][x + 1] = 1

        elif campus[y][x + 1] == "P":
            people_count += 1
            queue.append((y, x + 1))
            visited[y][x + 1] = 1

if people_count != 0:
    print(people_count)
else:
    print("TT")
