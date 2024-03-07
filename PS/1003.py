dp_list = [[0, 0] for _ in range(41)]
dp_list[0] = [1, 0]
dp_list[1] = [0, 1]

T = int(input())

for _ in range(T):
    i = 2
    N = int(input())
    while i <= N:
        dp_list[i][0] = dp_list[i - 1][0] + dp_list[i - 2][0]
        dp_list[i][1] = dp_list[i - 1][1] + dp_list[i - 2][1]
        i += 1
    print(dp_list[N][0], dp_list[N][1])
