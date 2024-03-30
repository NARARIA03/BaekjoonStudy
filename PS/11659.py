import sys

N, M = map(int, sys.stdin.readline().split())

# List 컴프리핸션을 사용해 입력받음
ary = list(map(int, sys.stdin.readline().split()))

# 입력받은 수들을 For문을 사용해 누적합으로 바꿔줌
for i in range(N - 1):
    ary[i + 1] = ary[i] + ary[i + 1]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    if a == 1:  # 만약 1부터 b까지 더해라 라는 식으로 나오면
        print(ary[b - 1])  # 더하라는 지점까지 더해둔 누적합
    elif a == b:  # 만약 1부터 1까지 더해라 라는 식으로 나오면
        print(ary[a - 1] - ary[a - 2])  # 구해야 하는 위치의 누적합 - 한칸 전 누적합
    else:  # 나머지 상황이면
        print(ary[b - 1] - ary[a - 2])  # 끝자리 까지 누적합 - 시작자리 - 1 까지 누적합
