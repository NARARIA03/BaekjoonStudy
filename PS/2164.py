from collections import deque

N = int(input())

ary = deque()

for i in range(1, N + 1):
    ary.append(i)

while 1:
    if len(ary) == 1:
        print(ary[0])
        break
    # ary.pop(0)
    # ary.append(ary.pop(0)) <- 시간 복잡도 문제로 초과가 난다.
    ary.popleft()
    ary.append(ary.popleft())
