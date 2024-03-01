import sys

stack = []
result_ary = []

def push(X):
    stack.append(X)

def pop():
    if (len(stack) == 0):
        result_ary.append(-1)
    else:
        result_ary.append(stack.pop())

def size():
    result_ary.append(len(stack))

def empty():
    if (len(stack) == 0):
        result_ary.append(1)
    else:
        result_ary.append(0)

def top():
    length = len(stack)
    if (length == 0):
        result_ary.append(-1)
    else:
        result_ary.append(stack[length - 1])

N = int(sys.stdin.readline())

for i in range(N):
    v = sys.stdin.readline()
    order = v.split()[0] # 입력 받은 값이 공백으로 구분된 2개라면, 앞에꺼 order에 저장, 공백이 없으면 그 값 그대로 order에 저장
    
    if (order == 'push'):
        num = int(v.split()[1]) # order가 push면, 입력받은 값이 공백으로 구분된 2개라는 뜻이고 공백 이후에 들어간 숫자를 정수로 바꿔 num에 저장
        push(num)
    elif (order == 'pop'):
        pop()
    elif (order == 'size'):
        size()
    elif (order == 'empty'):
        empty()
    elif (order == 'top'):
        top()
    else:
        continue

for v in result_ary:
    print(v)