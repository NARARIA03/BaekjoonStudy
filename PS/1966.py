import sys

c = int(sys.stdin.readline())
res_ary = []

for _ in range(c):
    # 찾으려는 값이 큐의 몇번째에 위치하는지에 대한 값 M
    _, M = map(int, sys.stdin.readline().split())
    queue = list(map(int, sys.stdin.readline().split()))
    count = 0

    while(1):
        flag = True
        for i in range(len(queue)):
            if (queue[i] > queue[0]):
                queue.append(queue.pop(0))
                flag=False
                if (M == 0):
                    M = len(queue) - 1
                else:
                    M -= 1
                break
            else:
                continue
        if (flag):
            queue.pop(0)
            count += 1
            if (M == 0):
                break
            else:
                M -= 1

    res_ary.append(count)

for res in res_ary:
    print(res)