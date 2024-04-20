N = int(input())

for _ in range(N):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)
    max_r = max(r1, r2)
    min_r = min(r1, r2)

    if dist == 0:
        if max_r == min_r:
            print(-1)
        else:
            print(0)
    else:
        if max_r + min_r == dist:
            print(1)
        elif max_r + min_r < dist:
            print(0)
        elif max_r + min_r > dist:
            if max_r - dist == min_r:
                print(1)
            elif dist + min_r < max_r:
                print(0)
            else:
                print(2)
