from sys import stdin

stack = [] # 스택
seq = [] # 수열
res = [] # 스택으로 만든 수열
ans = [] # + - 문자열
N = int(stdin.readline())
flag = True
index = 0

for i in range(N):
    seq.append(int(stdin.readline()))
num = sorted(seq) # 오름차순정렬된 수열 내 숫자

# 스택에 초기값 집어넣기
if (len(stack) == 0):
    stack.append(num.pop(0))
    ans.append('+')

# seq 만큼 체크
while (index < len(seq)):
    # 스택 비어있으면 push 수행
    if (len(stack) == 0):
        stack.append(num.pop(0))
        ans.append('+')
    
    # 스택의 마지막에 들어온 값이 seq의 현재 검사중인 값과 같으면 pop 수행하고 seq의 다음 값으로 이동
    elif (stack[-1] == seq[index]):
        res.append(stack.pop())
        ans.append('-')
        index += 1
        continue
    
    # 스택 마지막 값은 seq의 현재 검사중인 값과 다르고, num의 내부에 seq의 현재 검사중인 값이 존재하는 경우
    elif (seq[index] in num):
        # seq의 현재 검사중인 값이 num에서 없어질때까지 스택으로 push 수행
        while(seq[index] in num):
            stack.append(num.pop(0))
            ans.append('+')
        # num에 더 이상 seq의 현재 검사중인 값이 존재하지 않으면, 스택에서 pop 수행하고 seq의 다음 값으로 이동
        res.append(stack.pop())
        ans.append('-')
        index += 1
        continue
    
    # 어느경우에도 해당되지 않는 경우 flag를 False로 수정하고 while문 탈출 (당장 seq에 필요한 값이 스택 아래에 깔려있는 경우)
    else:
        flag = False
        break

if (flag):
    for i in ans:
        print(i)
else:
    print('NO') 
