N = int(input())
A = list(map(int, input().split()))
A = sorted(A)

M = int(input())
B = list(map(int, input().split()))

def binary_search(A, num):
    l = 0
    r = len(A) - 1
    while(l <= r):
        m = (l + r) // 2
        if (A[m] > num):
            r = m - 1
        elif (A[m] < num):
            l = m + 1
        else:
            print(1)
            return
    print(0)
    return

for num in B:
    binary_search(A, num)