import sys

sys.setrecursionlimit(10**7)


def check_paper(start_x, start_y, end_x, end_y):
    tmp = ary[start_y][start_x]
    for i in range(start_y, end_y + 1):
        for j in range(start_x, end_x + 1):
            if ary[i][j] != tmp:
                return False
    return True


def cutting_paper(start_x, start_y, end_x, end_y):
    global cnt_blue
    global cnt_white
    flag = check_paper(start_x, start_y, end_x, end_y)
    if flag:
        if ary[start_y][start_x] == 0:
            cnt_white += 1
        else:
            cnt_blue += 1
        return
    if start_x >= end_x or start_y >= end_y:
        if ary[start_y][start_x] == 0:
            cnt_white += 1
        else:
            cnt_blue += 1
        return

    mid_x = (start_x + end_x) // 2
    mid_y = (start_y + end_y) // 2

    cutting_paper(start_x, start_y, mid_x, mid_y)
    cutting_paper(mid_x + 1, start_y, end_x, mid_y)
    cutting_paper(start_x, mid_y + 1, mid_x, end_y)
    cutting_paper(mid_x + 1, mid_y + 1, end_x, end_y)


N = int(sys.stdin.readline())
ary = []

for _ in range(N):
    ary.append(list(map(int, sys.stdin.readline().rstrip().split())))

cnt_white = 0
cnt_blue = 0

cutting_paper(0, 0, N - 1, N - 1)
print(cnt_white)
print(cnt_blue)
