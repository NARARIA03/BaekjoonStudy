N, K = map(int, input().split())

ary = [i for i in range(1, N + 1)]

res_ary = []

idx = K - 1

while len(ary) > 0:
    res_ary.append(ary.pop(idx))
    idx = idx + K - 1

    if idx >= len(ary) and len(ary) != 0:
        idx = idx % len(ary)

if N == 1 and K == 1:
    print("<1>")
else:
    for i in range(0, len(res_ary)):
        if i == 0:
            print("<" + str(res_ary[i]) + ", ", end="")
        elif i == len(res_ary) - 1:
            print(str(res_ary[i]) + ">", end="")
        else:
            print(str(res_ary[i]) + ", ", end="")
