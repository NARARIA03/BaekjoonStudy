dp_list = [0 for _ in range(100)]
dp_list[0] = 0
dp_list[1] = 1

n = int(input())
i = 2

if n == 0 or n == 1:
    print(dp_list[n])
else:
    while i <= n:
        dp_list[i] = dp_list[i - 1] + dp_list[i - 2]
        i += 1
    print(dp_list[n])
