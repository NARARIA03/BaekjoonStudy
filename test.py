string = "[4]"
ary = []
start_idx = 0

for i in range(len(string)):
    if string[i] == "[":
        start_idx += 1
        continue
    if string[i] == ",":
        ary.append(int(string[start_idx:i]))
        start_idx = i + 1
        continue
    if string[i] == "]":
        if start_idx == 1:
            print("1로 끝")
        ary.append(int(string[start_idx:i]))
        break

print(ary)
