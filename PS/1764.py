import sys


N, M = map(int, sys.stdin.readline().split())

# 집합 선언은 set()를 사용한다.
no_hear_set = set()
no_see_set = set()

# 듣도 못한 사람의 이름 입력받아 no_hear_set에 추가. (list에선 append, set에선 add)
for _ in range(N):
    no_hear_set.add(sys.stdin.readline().strip())
# 보도 못한 사람의 이름 입력받아 no_see_set에 추가.
for _ in range(M):
    no_see_set.add(sys.stdin.readline().strip())

# 두 집합의 합집합을 계산해 union_set에 저장.
union_set = no_hear_set & no_see_set

# 집합의 길이 출력
sys.stdout.write(str(len(union_set)) + "\n")
# 집합 내 이름을 사전순으로 정렬해서 출력
for name in sorted(union_set):
    sys.stdout.write(name + "\n")
