N, M = map(int, input().split())
side_len = N if N < M else M
ary = []
for _ in range(N):
    num_list = list(map(int, input()))
    ary.append(num_list)

exit_flag = False
# print(ary)
while side_len > 0 and not exit_flag:
    for i in range(N - side_len + 1):
        if exit_flag:
            break
        for j in range(M - side_len + 1):
            if exit_flag:
                break
            vtx = ary[i][j]
            if (
                ary[i + side_len - 1][j] == vtx
                and ary[i + side_len - 1][j + side_len - 1] == vtx
                and ary[i][j + side_len - 1] == vtx
            ):
                print(side_len**2)
                exit_flag = True
    side_len -= 1
