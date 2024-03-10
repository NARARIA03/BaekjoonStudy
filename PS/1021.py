from collections import deque


# 왼쪽 회전 구현 함수
def left(queue):
    tmp = queue.popleft()
    queue.append(tmp)


# 오른쪽 회전 구현 함수
def right(queue):
    tmp = queue.pop()
    queue.appendleft(tmp)


N, M = map(int, input().split())

# 큐에서 deque 하고 싶은 값과 순서
want_list = list(map(int, input().split()))
queue = deque()
# 정답 값 저장 변수
result_value = 0

# 큐 초기화
for i in range(1, N + 1):
    queue.append(i)

# deque 하고 싶은 값 순서대로 하나씩 num에 저장
for num in want_list:
    idx = 0
    # num이 현재 queue에서 어디 위치하는지 찾기
    for i in range(len(queue)):
        if queue[i] == num:
            idx = i

    # num이 현재 좌측에 더 가깝다면 -> left 연산 수행해서 queue[0]까지 오도록 함
    if idx < len(queue) - idx:
        while queue[0] != num and len(queue) != 0:
            left(queue)
            result_value += 1
    # num이 현재 우측에 더 가깝다면 -> right 연산 수행해서 queue[0]까지 오도록 함
    else:
        while queue[0] != num and len(queue) != 0:
            right(queue)
            result_value += 1
    # queue[0]으로 옮긴 num을 deque 수행한다.
    queue.popleft()

# want_list에 대한 모든 값에 대해 left, right 연산을 수행한 횟수를 프린트한다
print(result_value)
