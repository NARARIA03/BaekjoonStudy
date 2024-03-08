def convert_num(value):
    return ord(value) - 96


_ = input()
string = list(input())

r = 31
m = 1234567891
i = 0
sum_value = 0
for char in string:
    sum_value += convert_num(char) * (r**i)
    i += 1
print(sum_value % m)
