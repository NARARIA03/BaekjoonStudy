from collections import deque

# 수빈이가 술래
# N = 수빈이 위치, K = 동생의 위치
N, K = map(int, input().split())

queue = deque()
queue.append(N)
# 몇 번만에 찾았는지 기록할 변수
cnt = 0
# K를 찾았으면 종료하기 위한 flag
flag = False
# 특정 숫자에 대한 방문 체크를 위한 배열
# 방문 체크를 하지 않으면, 이전에 계산했던 값에 대한 트리가 계속 펼쳐져서 너무 커진다 -> 큐 메모리 초과
# 아래 visited 배열 선언을 [0 for _ in range(100001)]로 하면 틀렸는데, 아래처럼 크게 하니까 맞는다..?
visited = [0 for _ in range(10000000)]

while 1:
    length = len(queue)
    for _ in range(length):
        v = queue.popleft()
        if v == K:
            flag = True
            break
        # v + 1, v - 1, v * 2가 문제에서 제한해준 100000을 넘는지 확인해준다.
        # 만약 v + 1, v - 1, v * 2 값이 100000을 넘게 되면, visited 배열에 접근하면서 index가 범위를 벗어나기 때문
        if v + 1 <= 100000 and visited[v + 1] == 0:
            queue.append(v + 1)
            visited[v + 1] = 1
        if v - 1 <= 100000 and visited[v - 1] == 0:
            queue.append(v - 1)
            visited[v - 1] = 1
        if v * 2 <= 100000 and visited[v * 2] == 0:
            queue.append(v * 2)
            visited[v * 2] = 1
    if flag:
        break
    cnt += 1
print(cnt)
