# 에라토스테네스의 체로 구현, 시간 복잡도는 O(N^(1/2))
M, N = map(int, input().split())

# 먼저 0 ~ N까지 값이 저장된 (인덱스와 값이 일치하는) 리스트 생성
num_list = [int(i) for i in range(0, N + 1)]
# 1번 인덱스의 값 1은 소수가 아니므로 0 처리
num_list[1] = 0
# 각 수가 갖는 약수는 해당 수의 제곱근을 기준으로 대칭을 이루기 때문에 루트N까지만 에라토스테네스의 체를 적용
end = int(N ** (1/2))

# 2 부터 루트N까지 반복
for i in range(2, end + 1):
		# i 인덱스에 저장된 값이 0이면 이미 체로 걸러진것이므로 continue
    if (num_list[i] == 0):
        continue
    else:
				# i 인덱스에 저장된 값이 0이 아니면, i를 제외한 i의 배수를 전부 0으로 변경
				# 시작값이 i * 2고, 매 회 i씩 더해가며 N까지 전부 체로 걸러낸다고 보면 된다.
        for j in range(i + i, N + 1, i):
            num_list[j] = 0
# 전부 걸러냈으므로, 이제 문제에서 주어진 시작지점부터 끝지점까지 값이 0이 아닌 애들만 print해준다
for i in range(M, N+1):
    if (num_list[i] != 0):
        print(num_list[i])