def factorial(num):
    if (num == 1 or num == 0):
        return 1
    else:
        return num * factorial(num - 1)

N = int(input())

num = factorial(N)

if (num % 10 != 0):
    print(0)
else:
    res = 1
    while(1):
        if (num % 10 ** (res + 1) == 0):
            res += 1
            continue
        else:
            print(res)
            break
