while 1:
    string = input()
    if string == ".":
        break
    stack = []

    for char in string:
        if char == "(" or char == "[" or char == ")" or char == "]":
            stack.append(char)

        if len(stack) >= 2:
            if stack[-1] == ")" and stack[-2] == "(":
                stack.pop()
                stack.pop()
            elif stack[-1] == "]" and stack[-2] == "[":
                stack.pop()
                stack.pop()
    if len(stack) == 0:
        print("yes")
    else:
        print("no")
