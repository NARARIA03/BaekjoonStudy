from collections import deque


def swap_queue():
    queue.append(queue.popleft())


N, K = map(int, input().split())

queue = deque()
res_ary = []

for i in range(1, N + 1):
    queue.append(i)

while queue:
    for _ in range(K - 1):
        swap_queue()
    res_ary.append(queue.popleft())

print("<", end="")
for i in range(len(res_ary)):
    if i != len(res_ary) - 1:
        print(res_ary[i], end=", ")
    else:
        print(res_ary[i], end="")
print(">")
