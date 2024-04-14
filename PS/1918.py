from collections import deque

l = list(input())
stack = deque()

for char in l:
    if char >= "A" and char <= "Z":
        print(char, end="")
    elif char == "(":
        stack.append(char)
    elif char == ")":
        while stack[-1] != "(":
            print(stack.pop(), end="")
        stack.pop()
    elif char == "+" or char == "-":
        while len(stack) > 0 and (
            stack[-1] == "+" or stack[-1] == "-" or stack[-1] == "*" or stack[-1] == "/"
        ):
            print(stack.pop(), end="")
        stack.append(char)
    elif char == "*" or char == "/":
        while len(stack) > 0 and (stack[-1] == "*" or stack[-1] == "/"):
            print(stack.pop(), end="")
        stack.append(char)

while stack:
    print(stack.pop(), end="")
