T = int(input())
result = []

for i in range(T):
    H, W, N = map(int, input().split()) # H = 층수(높이), W = 방수 (가로), N = 몇 번째 손님의 방을 찾아줄것인지
    if (N > H):
        if (N % H != 0):
            res = (N % H) * 100
            res = res + (N // H + 1)
        else:
            res = H * 100
            res = res + (N // H)
        result.append(res)
    elif (N <= H):
        res = N * 100 + 1
        result.append(res)

for i in result:
    print(i)