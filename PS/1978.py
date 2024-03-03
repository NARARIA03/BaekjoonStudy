_ = int(input())

num_list = map(int, input().split())

cnt = 0

for num in num_list:
    if (num == 1):
        continue
    else:
        flag = True
        for i in range(2, num):
            if (num % i == 0):
                flag = False
        if (flag):
            cnt += 1

print(cnt)