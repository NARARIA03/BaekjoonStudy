N = int(input())

# 리스트 컴프리핸션을 사용해서 2차원 인접 행렬 입력받기
adj_ary = [list(map(int, input().split())) for _ in range(N)]


# 플로이드 워셜 알고리즘으로 모든 정점에 대해, 모든 정점까지의 최소 거리를 구한다.
def floyd_warshall():
    # 모든 값이 무한대로 초기화된, adj_ary와 동일한 크기의 2차원 배열 생성.
    dist = [[float("inf") for _ in range(N)] for _ in range(N)]

    # 인접 행렬에서 두 정점이 연결되었다는 것이 확인되면, dist 배열에서 거리값을 1로 수정.
    # 이 문제는 그동안 풀던 그래프 문제와 다르게, 양방향 그래프가 아니라 방향 그래프이다. 즉 [i][j] == 1 이어도, [j][i] != 1 일 수 있다.
    for i in range(N):
        for j in range(N):
            if adj_ary[i][j] == 1:
                dist[i][j] = 1
                # dist[j][i] = 1 단방향이므로!

    # 플로이드 워셜 알고리즘 시작.
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


res_ary = floyd_warshall()

# 플로이드 워셜 알고리즘 실행 결과가 inf라면, 연결된 간선이 없다는 것 -> 0 입력, inf가 아니라면 1 입력.
for i in range(N):
    for j in range(N):
        if res_ary[i][j] == float("inf"):
            res_ary[i][j] = 0
        else:
            res_ary[i][j] = 1

# 입력된 최종 결과를 양식에 맞게 출력한다.
for row in res_ary:
    print(*row)
