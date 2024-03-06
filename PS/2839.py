N = int(input())

cnt = 10000000

for i in range(N // 5 + 1):
    for j in range(N // 3 + 1):
        if i * 5 + j * 3 == N and cnt > i + j:
            cnt = i + j
if cnt == 10000000:
    print(-1)
else:
    print(cnt)
