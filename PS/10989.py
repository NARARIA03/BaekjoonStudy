import sys

N = int(sys.stdin.readline().strip())
num_ary = [0 for _ in range(10001)]

for i in range(N):
    num = int(sys.stdin.readline().strip())
    num_ary[num] += 1


for i in range(1, 10001):
    if num_ary[i] > 0:
        while num_ary[i] > 0:
            sys.stdout.write(str(i) + "\n")
            num_ary[i] -= 1
