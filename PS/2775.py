import sys

# dp용으로 15 by 15 2차원 리스트 생성, 전부 0을 채워뒀다.
dp_list = [[0 for _ in range(15)] for _ in range(15)]


# k = 층수 (0부터 시작)
# n = 호수 (1부터 시작)
def dp_apt_people_count(k, n):
    # 0층 n호 값 반환
    if k == 0:
        return dp_list[0][n]
    # 1층 이상 n호 값 반환
    else:
        floor = 1
        # k층 n호까지 dp 사용해 계산
        while floor <= k:
            for i in range(1, n + 1):
                dp_list[floor][i] = dp_list[floor][i - 1] + dp_list[floor - 1][i]
            floor += 1
        return dp_list[k][n]


T = int(sys.stdin.readline())

# 0층 초기화
for i in range(1, 15):
    dp_list[0][i] = i

for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    res = dp_apt_people_count(k, n)
    sys.stdout.write(str(res) + "\n")


# # 참고 (재귀 구현, 시간초과)
# def apt_people_count(k, n):
#     # 재귀 코드
#     if k == 0:
#         return n
#     else:
#         sum = 0
#         for i in range(1, n + 1):
#             sum += apt_people_count(k - 1, i)
#         return sum
