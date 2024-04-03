a, b, c, d, e, f = map(int, input().split())

flag = False
for x in range(-999, 1000):
    if flag:
        break
    for y in range(-999, 1000):
        if flag:
            break
        if a * x + b * y == c and d * x + e * y == f:
            print(x, y)
            flag = True
