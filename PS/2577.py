num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

a = int(input())
b = int(input())
c = int(input())

res = a * b * c
res_string = str(res)

for num in range(0, 10):
    cnt = 0
    for char in res_string:
        if (char == str(num)):
            cnt = cnt + 1
    print(cnt)
