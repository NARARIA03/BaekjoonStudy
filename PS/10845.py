import sys

queue = []
res_ary = []

def push(X):
    queue.append(X)

def pop():
    if (len(queue) == 0):
        res_ary.append(-1)
    else:
        res_ary.append(queue.pop(0))

def size():
    res_ary.append(len(queue))

def empty():
    if (len(queue) == 0):
        res_ary.append(1)
    else:
        res_ary.append(0)

def front():
    if (len(queue) == 0):
        res_ary.append(-1)
    else:
        res_ary.append(queue[0])

def back():
    if (len(queue) == 0):
        res_ary.append(-1)
    else:
        res_ary.append(queue[len(queue) - 1])

N = int(sys.stdin.readline())

for i in range(N):
    v = sys.stdin.readline().split()

    if (v[0] == 'push'):
        push(v[1])
    elif (v[0] == 'pop'):
        pop()
    elif (v[0] == 'size'):
        size()
    elif (v[0] == 'empty'):
        empty()
    elif (v[0] == 'front'):
        front()
    elif (v[0] == 'back'):
        back()
    else:
        continue

for res in res_ary:
    print(res)