N, x = map(int, input().split(" "))
ary = []

for _ in range(N + 1):
    ary.append(int(input().split(" ")[0]))

sol = ary[0]

for i in range(1, N + 1):
    sol = (sol * x + ary[i]) % 1000000007

print(sol)
