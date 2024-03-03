def is_right_triangle(a, b, c):
    flag = False
    h = max(a, b, c)

    if a == h and b != h and c != h:
        if h**2 == b**2 + c**2:
            flag = True
    elif b == h and a != h and c != h:
        if h**2 == a**2 + c**2:
            flag = True
    elif c == h and a != h and b != h:
        if h**2 == a**2 + b**2:
            flag = True

    if flag:
        print("right")
    else:
        print("wrong")


while 1:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    is_right_triangle(a, b, c)
