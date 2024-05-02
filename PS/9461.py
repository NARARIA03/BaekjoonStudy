DP_ary = [1, 1, 1]

while len(DP_ary) < 100:
    DP_ary.append(DP_ary[-2] + DP_ary[-3])

# print(DP_ary)

T = int(input())

for _ in range(T):
    N = int(input())
    print(DP_ary[N - 1])
