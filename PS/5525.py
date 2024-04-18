N = int(input())
M = int(input())
S = input()

pn_string = "IO" * N + "I"
# print(pn_string)

i = 0
cnt = 0
while i <= M - (2 * N + 1):
    if S[i] == "O":
        i += 1
        continue
    elif S[i] == "I":
        if S[i : i + (2 * N + 1)] == pn_string:
            cnt += 1
            i += 2
        else:
            i += 1

print(cnt)
