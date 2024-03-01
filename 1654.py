K, N = map(int, input().split())
ary = []

for i in range(K):
    ary.append(int(input()))

l = 1
r = max(ary)
m = (l + r) // 2

while(l <= r):
    m = (l + r) // 2
    s = 0
    for i in ary:
        s = s + (i // m)

    if (s >= N):
        l = m + 1
    elif (s < N):
        r = m - 1

print(r)
