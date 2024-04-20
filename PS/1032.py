N = int(input())
ary = []

for _ in range(N):
    ary.append(input())

# print(ary)
res = ""
length = len(ary[0])

for i in range(length):
    flag = False
    tmp = ary[0][i]
    # print("ary[0][i]: ", tmp)
    for name in ary:
        if name[i] == tmp:
            continue
        else:
            flag = True
            break
    if flag:
        res += "?"
    else:
        res += ary[0][i]


print(res)
