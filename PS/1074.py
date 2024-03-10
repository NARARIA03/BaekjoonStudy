import sys

sys.setrecursionlimit(10**8)
# 방문할 때 집어넣을 숫자 <- 전역 변수로 가져와 사용한다.
count = 0


def recursion_z(n, min_x, min_y):
    global count
    # n == 1이라는 것은, 사분면을 쪼개 탐색해오면서 2차원 가상 배열의 크기를 / 2 해왔는데,
    # 이 가상 배열의 크기가 2 by 2가 되었다는 뜻이다.
    if n == 1:
        if min_y == r and min_x == c:
            # 가상 배열의 좌상단 index가 문제의 index와 같다면
            print(count)
        elif min_y == r and min_x + 1 == c:
            # 가상 배열의 우상단 index가 문제의 index와 같다면
            # count 값 1증가 ( Z ) 모양으로 1씩 커지므로..
            count += 1
            print(count)
        elif min_y + 1 == r and min_x == c:
            # 가상 배열의 좌하단 index가 문제의 index와 같다면
            # count 값 2 증가
            count += 2
            print(count)
        elif min_y + 1 == r and min_x + 1 == c:
            # 가상 배열의 우하단 index가 문제의 index와 같다면
            # count 값 3 증가
            count += 3
            print(count)
    # 가상 배열을 쪼개는 단계 (아직 2 by 2까지 작아지기 전)
    # 현재 가상 배열의 몇 사분면에 virtual_ary[r][c]가 위치하는지
    # 즉 [r][c]는 몇 사분면인지 if문으로 가려낸 뒤, 해당 사분면으로 가상 배열을 축소하며 재귀를 돌린다
    elif n > 1:
        # 1 사분면에 r, c 포함
        if 0 <= r < min_y + 2 ** (n - 1) and 0 <= c < min_x + 2 ** (n - 1):
            # Top - Left
            # n 값을 1 줄이고, min_x, min_y를 1 사분면에 맞게 조절해준다
            recursion_z(n - 1, min_x, min_y)
        # 2 사분면에 r, c 포함
        elif 0 <= r < min_y + 2 ** (n - 1) and min_x + 2 ** (n - 1) <= c:
            # Top - Right
            # n 값을 1 줄이고, min_x, min_y를 2 사분면에 맞게 (min_y는 그대로, min_x는 키워준다) 조절해준다
            # 1사분면 안에 들어갈 숫자 수를 count에 더해서 건너뛰어준다
            count += (2 ** (n - 1)) ** 2
            recursion_z(n - 1, min_x + 2 ** (n - 1), min_y)
        # 3 사분면에 r, c 포함
        elif min_y + 2 ** (n - 1) <= r and 0 <= c < min_x + 2 ** (n - 1):
            # Bottom - Left
            # n 값을 1 줄이고, min_x, min_y를 3 사분면에 맞게 (min_y는 키우고, min_x는 그대로) 조절해준다
            # 1, 2 사분면 안에 들어갈 숫자 수를 count에 더해서 건너뛰어준다
            count += 2 * ((2 ** (n - 1)) ** 2)
            recursion_z(n - 1, min_x, min_y + 2 ** (n - 1))
        elif min_y + 2 ** (n - 1) <= r and min_x + 2 ** (n - 1) <= c:
            # Bottom - Right
            # n 값을 1 줄이고, min_x, min_y를 4 사분면에 맞게 (min_y와 min_x 모두 키운다) 조절해준다
            # 1, 2, 3 사분면 안에 들어갈 숫자 수를 count에 더해서 건너뛰어준다
            count += 3 * ((2 ** (n - 1)) ** 2)
            recursion_z(n - 1, min_x + 2 ** (n - 1), min_y + 2 ** (n - 1))


# n : 배열의 크기를 결정 (2^n by 2^n)
# r, c : r행 c열에 몇 번째로 방문하는지 (problem)
n, r, c = map(int, sys.stdin.readline().split())
recursion_z(n, 0, 0)
