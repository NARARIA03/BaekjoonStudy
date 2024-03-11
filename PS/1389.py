# N = 유저의 수, M = 관계의 수 (반복문에 사용)
N, M = map(int, input().split())

# 인접 행렬 (i 노드와 j 노드가 연결되었다면, adjacency_matrix[i][j] == 1 and adjacency_matrix[j][i] == 1 이다.)
adjacency_matrix = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

# 특정 노드가 연결되었다는 정보를 M 번 받아, adjacency_matrix에 저장
for _ in range(M):
    p1, p2 = map(int, input().split())
    adjacency_matrix[p1][p2] = 1
    adjacency_matrix[p2][p1] = 1


# 플로이드 워셜 알고리즘 (다익스트라 알고리즘과 달리 모든 정점에 대해, 모든 정점까지 최단거리를 한 번에 구하는 알고리즘)
# 다익스트라 알고리즘은 distance 배열이 1차원이지만(한 정점에 대해, 모든 정점까지 최단거리를 구하므로)
# 플로이드 워셜 알고리즘은 distance 배열이 2차원이다. (모든 정점에 대해, 모든 정점까지 최단거리를 구하므로)
def floyd_warshall():
    # float("inf")로 무한대값 표현 가능
    # distance = 거리 배열
    distance = [[float("inf") for _ in range(N + 1)] for _ in range(N + 1)]
    # 만약 노드 i와 노드 j가 직접 연결되어 있다면 distance[i][j]와 distance[j][i]를 해당 거리값(1)으로 초기화
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if adjacency_matrix[i][j] == 1 and adjacency_matrix[j][i] == 1:
                distance[i][j] = 1
                distance[j][i] = 1

    # 여기서부터 플로이드 워셜 알고리즘을 distance 배열에 대해 동작시킨다.
    # 플로이드 워셜 알고리즘은 DP적인 특성을 가진다, 때문에 경유지로 사용하는 k가 가장 바깥 반복문에 위치해야 모든 경로 중 최소값을 택할 수 있다.
    # 더 쉽게 말하면, 초기화가 되지 않은 상태의 [i][k]는 무한대의 거리를 갖지만, 후에 반복을 하면서 [i][k]의 거리가 줄어들 수 있다.
    # 그렇기 때문에 순서를 잘 지키지 않으면, [i][k]가 제대로 구해지지 않은 상태, 즉 무한대인 상황에서 거리를 확인하게 되어 연쇄적으로 값이 무너질 수 있다.
    # 이런 이유가 있지만, 결론은 "경유지노드 index를 가장 바깥 for문에 배치해 사용해야 한다"는 점만 기억하면 된다.
    # k -> i -> j : [i][j] > [i][k] + [k][j] 이 수식들만 기억해도 구현에 문제는 없을 것이다.
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if k == j:
                    continue
                elif distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
    return distance


# sol 이라는 변수에 플로이드 워셜 알고리즘 수행 결과를 저장한다.
sol = floyd_warshall()
result_ary = []

# 플로이드 워셜 알고리즘 수행 결과인 2차원 배열을 2중 반복문으로 접근해서 한 행에 저장된 값을 무한대 제외하고 모두 더해준다.
# 그리고 한 행을 더하면, result_ary에 append 해준다.
for row in sol:
    sum = 0
    for num in row:
        if num == float("inf"):
            continue
        sum += num
    result_ary.append(sum)
# 생각해보면, index와 노드의 번호를 맞추기 위해 distance 배열의 0행과 0열은 모두 무한대로 초기화가 되어 있었다.
# 이를 반환해서 sum에 무한대가 아니면 더하기를 수행했으므로, result_ary의 0번째 인덱스에는 0이라는 필요 없는 값이 저장되어 있다.
# 따라서 이를 pop으로 제거해준다.
result_ary.pop(0)
# 배열.index(값) 수식을 통해 값이 존재하는 가장 작은 index를 반환해서, 여기에 1을 더해 정답을 출력한다.
print(result_ary.index(min(result_ary)) + 1)
