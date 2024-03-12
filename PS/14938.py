# n = 지역의 개수, m = 수색범위, r = 길의 개수
# 지역의 번호는 1 이상 n 이하의 정수이다. 두 지역의 번호가 같은 경우는 없다.
n, m, r = map(int, input().split())

# 각 지역의 아이템 수, 지역의 번호에서 - 1 한 index로 접근해야 한다
item_ary = list(map(int, input().split()))

# 인접행렬 및 가중치배열 생성 및 초기화
adj_ary = [[float("inf") for _ in range(n + 1)] for _ in range(n + 1)]

# 이 문제에서의 그래프는 양방향 가중치 그래프이다.
for _ in range(r):
    a, b, l = map(int, input().split())
    # 혹시 더 짧은 길을 나중에 줄 수도 있으니까
    if adj_ary[a][b] > l:
        adj_ary[a][b] = l
        adj_ary[b][a] = l

# 플로이드 워셜 알고리즘을 사용해 모든 정점에서 다른 모든 정점까지 가는데 들어가는 수색범위 값을 체크한다
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # 자기자신으로 돌아오는 경로의 길이 최소값은 필요가 없으므로 0으로 잡아준다
            if i == j:
                adj_ary[i][j] = 0
            # 자기자신 경로를 제외하고는 플로이드 워셜 알고리즘으로 최소경로를 구해준다
            elif adj_ary[i][j] > adj_ary[i][k] + adj_ary[k][j]:
                adj_ary[i][j] = adj_ary[i][k] + adj_ary[k][j]

# 모든 노드에 착지해보았을 때 얻을 수 있는 아이템의 최대 수
# 모든 지역의 아이템 수는 1 이상 30 이하이므로 초기화는 0으로 해도 된다
max_sum = 0
for i in range(1, n + 1):
    # 한 노드에 착지해보았을 때 얻을 수 있는 아이템의 최대 수
    sum = 0
    for j in range(1, n + 1):
        # 수색 범위가 해당 지역까지 가는 길의 가중치 이상 -> 해당 지역으로 이동 가능 -> 해당 지역의 아이템 획득 가능
        if adj_ary[i][j] <= m:
            sum += item_ary[j - 1]  # 해당 지역의 아이템 수를 sum에 합해준다
    max_sum = max(max_sum, sum)

print(max_sum)
