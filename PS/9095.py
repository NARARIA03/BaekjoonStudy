dp = [0, 1, 2, 4]


def calculate_hap_count(dest):
    start = len(dp)

    while start <= dest:
        sum = dp[start - 1] + dp[start - 2] + dp[start - 3]
        dp.append(sum)
        start += 1

    return dp[dest]


T = int(input())

for _ in range(T):
    n = int(input())
    result = calculate_hap_count(n)
    print(result)
