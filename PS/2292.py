res = 1
l = r = 1
N = int(input())

while 1:
    if l <= N and N <= r:
        print(res)
        break
    else:
        res += 1
        l = r + 1
        r = (l + (res - 1) * 6) - 1
