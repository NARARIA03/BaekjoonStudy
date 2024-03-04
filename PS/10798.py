ary = [list(input()) for _ in range(5)]

max_length = 0

for i in range(5):
    if max_length <= len(ary[i]):
        max_length = len(ary[i])

for i in range(max_length):
    for j in range(5):
        if len(ary[j]) - 1 >= i:
            print(ary[j][i], end="")
        else:
            continue