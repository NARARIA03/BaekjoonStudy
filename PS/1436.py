N = int(input())
cnt = 1
num = 666

while (cnt < N):
    num += 1
    list_num = list(str(num))
    for i in range(0, len(list_num) - 2, 1):
        if (list_num[i] == '6' and list_num[i + 1] == '6' and list_num[i + 2] == '6'):
            cnt += 1
            break
        else:
            continue

print(num)