A, B = map(str, input().split())

res = 0
for i in A:
    for j in B:
        res += int(i) * int(j)
print(res)
