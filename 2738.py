N, M = map(int, input().split())

# 리스트 컴프리헨션을 사용해 2차원 리스트에 입력 받기
A = [[int(num) for num in input().split()] for y in range(N)]

# 반복문을 사용해 2차원 리스트에 입력 받기
B = []
for n in range(N):
    row = list(map(int, input().split()))
    B.append(row)

# 리스트 컴프리헨션을 사용해 0으로 채워진 2차원 배열 생성
result = [[0 for x in range(M)] for y in range(N)]

# 이중 for문으로 더한 값 저장
for y in range(N):
    for x in range(M):
        result[y][x] = A[y][x] + B[y][x]

# 문제 양식에 맞게 출력
for y in range(N):
    for x in range(M):
        print(result[y][x], end=" ")
    print()