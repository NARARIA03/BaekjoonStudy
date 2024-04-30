chess_ary = []

for _ in range(8):
    row = input()
    chess_ary.append(row)

res = 0
for i in range(8):
    for j in range(8):
        if chess_ary[i][j] == "F" and (
            (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1)
        ):
            res += 1
print(res)
