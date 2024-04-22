import sys

mod_ary = []

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    mod_ary.clear()
    a, b = map(int, sys.stdin.readline().split())
    mod_ary.append(a % 10)
    i = 2
    mul = ((a % 10) ** 2) % 10
    while i <= b and mod_ary[0] != mul:
        mod_ary.append(mul)
        i += 1
        mul = (mul * (a % 10)) % 10
    # print("mod_ary: ", mod_ary)
    sol_idx = b % len(mod_ary) - 1
    # print("sol: ", mod_ary[sol_idx])
    # print(mod_ary[sol_idx])
    if mod_ary[sol_idx] == 0:
        sys.stdout.write("10\n")
    else:
        sys.stdout.write(str(mod_ary[sol_idx]) + "\n")
