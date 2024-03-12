import sys
from collections import deque

# 리스트를 사용해야 했는데, pop(0)을 많이 하면 시간초과가 걱정되서 deque 사용
N = int(sys.stdin.readline())
ary = deque()
ary.append(N)
flag = False
cnt = 0

# 만약 초기 입력값이 1이라면 while문 실행 X
if N == 1:
    flag = True

# ary에 1이 존재하지 않는다면 while문 실행
while not flag:
    # 연산 횟수 1 증가
    cnt += 1
    # 이번 Phase에서 ary에 들어있는 원소의 수 기록
    length = len(ary)

    # 이번 Phase에서 ary에 들어있는 원소 수 만큼만 반복
    for _ in range(length):
        v = ary.popleft()  # deque 수행
        # v가 2로 나누어떨어진다면
        if v % 2 == 0:
            ary.append(v / 2)  # 2로 나눈 결과를 ary에 append
        # v가 3으로 나누어떨어진다면
        if v % 3 == 0:
            ary.append(v / 3)  # 3으로 나눈 결과를 ary에 append
        # v - 1을 해도 1보다 크거나 같다면
        if v - 1 >= 1:
            ary.append(v - 1)  # v - 1 수행한 결과를 ary에 append
    # 현재 Phase에서 수행 가능한 모든 연산을 수행한 결과들 중 1이 존재하는지 확인
    for res in ary:
        if res == 1:  # 1이 존재한다면
            flag = True  # 다음 Phase 실행 전에 반복문 탈출
            break
print(cnt)
