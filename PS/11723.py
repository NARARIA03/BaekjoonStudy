import sys

s = set()

all = set([i for i in range(1, 21)])

M = int(sys.stdin.readline().rstrip())

for _ in range(M):
    order = sys.stdin.readline().rstrip()
    if order == "all":
        # 얕은 복사, 깊은 복사에 주의!
        # s = all 과 같이 사용해버리면, s의 포인터와 all의 포인터가 같아지게 된다.
        # 따라서 이후 수정 메소드가 입력되면 all의 데이터가 직접적으로 수정되게 되서
        # 다시 all을 수행해도 1~20이 들어있는 집합을 가져올 수 없게 된다.
        s = all.copy()
    elif order == "empty":
        s.clear()
    else:
        func, num = order.split()
        num = int(num)
        if func == "add":
            if num not in s:
                s.add(num)
        elif func == "remove":
            if num in s:
                s.discard(num)
        elif func == "check":
            if num in s:
                print(1)
            else:
                print(0)
        elif func == "toggle":
            if num in s:
                s.discard(num)
            else:
                s.add(num)
