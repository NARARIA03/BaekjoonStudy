# 특정 알파벳 아스키코드에서 97을 뺀 숫자 == 알파벳 리스트의 인덱스
char_list = [0 for _ in range(26)]
S = input()

for char in S:
    char_list[ord(char) - 97] += 1

print(*char_list)
