# 연산은 두 가지 종류가 가능
# *2 또는 1을 수의 가장 오른쪽에 추가 (*10 + 1)
from collections import deque

visited = []

A, B = map(int, input().split())
queue = deque()
queue.append(A)
visited.append(A)
cnt = 0
is_success = False

while queue:
    if is_success:
        break
    length = len(queue)
    for _ in range(length):
        num = queue.popleft()
        # print("num: ", num)
        if num == B:
            is_success = True
            break
        if num * 2 <= B and (num * 2 not in visited):
            queue.append(num * 2)
            visited.append(num * 2)

        if num * 10 + 1 <= B and (num * 10 + 1 not in visited):
            queue.append(num * 10 + 1)
            visited.append(num * 10 + 1)
    cnt += 1

if is_success:
    print(cnt)
else:
    print(-1)
