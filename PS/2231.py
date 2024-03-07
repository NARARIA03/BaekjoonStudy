N = int(input())

num = 1

while 1:
    if num == N:
        print(0)
        break
    tmp = num
    num_list = list(str(num))
    for num_char in num_list:
        tmp = tmp + int(num_char)
    if tmp == N:
        print(num)
        break
    else:
        num += 1
