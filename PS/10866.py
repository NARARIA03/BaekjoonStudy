import sys

dequeue = []
res_ary = []

def push_front(X):
    # 리스트의 맨 앞에 아이템을 추가하려면 insert(0, item)으로 구현 가능하다.
    dequeue.insert(0, X)

def push_back(X):
    dequeue.append(X)

def pop_front():
    if (len(dequeue) == 0):
        res_ary.append(-1)
    else:
        res_ary.append(dequeue.pop(0))

def pop_back():
    if (len(dequeue) == 0):
        res_ary.append(-1)
    else:
        res_ary.append(dequeue.pop(len(dequeue) -1))

def size():
    res_ary.append(len(dequeue))

def empty():
    if (len(dequeue) == 0):
        res_ary.append(1)
    else:
        res_ary.append(0)

def front():
    if (len(dequeue) == 0):
        res_ary.append(-1)
    else:
        res_ary.append(dequeue[0])

def back():
    if (len(dequeue) == 0):
        res_ary.append(-1)
    else:
        res_ary.append(dequeue[len(dequeue) - 1])

N = int(sys.stdin.readline())

for _ in range(N):
    v = sys.stdin.readline().split()
    if (v[0] == 'push_front'):
        push_front(v[1])
    elif (v[0] == 'push_back'):
        push_back(v[1])
    elif (v[0] == 'pop_front'):
        pop_front()
    elif (v[0] == 'pop_back'):
        pop_back()
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