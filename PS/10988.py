string = input()

max_idx = len(string) // 2
i = 0
sol = 1

while i < max_idx:
    if string[i] == string[-(1 + i)]:
        i += 1
        continue
    else:
        sol = 0
        break
print(sol)
