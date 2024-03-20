# A : 65
# Z : 90
# a : 97
# z : 122

string = input()
res = []
for char in string:
    ascii = ord(char)
    if 65 <= ascii <= 90:
        res.append(chr(ascii + 32))
    else:
        res.append(chr(ascii - 32))

for char in res:
    print(char, end="")
