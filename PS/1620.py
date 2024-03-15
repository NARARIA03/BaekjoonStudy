import sys

# N = 도감에 수록된 포켓몬 수
# M = 맞춰야 하는 문제의 수

N, M = map(int, sys.stdin.readline().split())

dictionary = {}
for i in range(1, N + 1):
    pokemon = sys.stdin.readline().strip()
    dictionary[pokemon] = str(i)
    dictionary[str(i)] = pokemon

for _ in range(M):
    test_case = sys.stdin.readline().strip()
    sys.stdout.write(dictionary[test_case] + "\n")

# ary.index(value) 이거 자체가 O(N)이라 N^2으로 시간 초과 발생
# 딕셔너리로 접근이 가능하다
# isdigit이라는 함수가 존재한다
