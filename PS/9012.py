N = int(input())
res_ary = []

for _ in range(N):
    stack = []
    problem = list(input())
    for char in problem:
        stack.append(char)
        if len(stack) > 1:
            if stack[-1] == ")" and stack[-2] == "(":
                stack.pop()
                stack.pop()

    if len(stack) == 0:
        res_ary.append("YES")
    else:
        res_ary.append("NO")

for res in res_ary:
    print(res)
