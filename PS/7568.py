N = int(input())

xy_list = [[0, 0] for _ in range(N)]
result_ary = []

for i in range(N):
    xy_list[i][0], xy_list[i][1] = map(int, input().split())

for i in range(N):
    cnt = 0
    for j in range(N):
        if xy_list[i][0] < xy_list[j][0] and xy_list[i][1] < xy_list[j][1]:
            cnt += 1
    result_ary.append(cnt + 1)

print(*result_ary)
