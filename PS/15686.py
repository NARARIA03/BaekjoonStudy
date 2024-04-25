from itertools import combinations


# map 배열을 입력받아 치킨집의 y, x 인덱스 쌍을 모아둔 배열을 반환
def return_market_idx(maps: list):
    idx_ary = []
    for y in range(N):
        for x in range(N):
            if maps[y][x] == 2:
                idx_ary.append((y, x))
    return idx_ary


# map 배열을 입력받아 집의 y, x 인덱스 쌍을 모아둔 배열을 반환
def return_home_idx(maps: list):
    idx_ary = []
    for y in range(N):
        for x in range(N):
            if maps[y][x] == 1:
                idx_ary.append((y, x))
    return idx_ary


# itertools의 combinations 함수를 사용해
# 치킨집 중 몇 개 폐업하고 남길 수 있는 모든 경우의 수를 저장해 반환
# nCr에서 itertools.combinations(list, r)과 같이 사용
def return_combination_market_idx(idx_ary: list):
    combination = list(combinations(idx_ary, M))
    return combination


# 문제에서 주어지는 지도 저장 배열
maps = []
N, M = map(int, input().split())
for _ in range(N):
    maps.append(list(map(int, input().split())))

# 치킨집 인덱스 쌍 배열 구하기
market_idx_ary = return_market_idx(maps)
# 치킨집 인덱스 쌍 배열에서 M개만 남기고 폐업시키는 모든 시나리오 구하기
market_combination_idx_ary = return_combination_market_idx(market_idx_ary)
# 집 인덱스 쌍 구하기
home_idx_ary = return_home_idx(maps)

city_chicken_dist_scenario_ary = []
# 모든 치킨집 폐업 시나리오 반복
for i in range(len(market_combination_idx_ary)):
    # 치킨집을 M개만 남긴 케이스 하나에 대해 도시의 치킨 거리 계산용 변수
    city_chicken_dist = 0
    for j in range(len(home_idx_ary)):
        # 모든 집 인덱스 쌍 중 하나를 선택
        home_y, home_x = home_idx_ary[j]
        # 해당 집에 대한 치킨 거리를 계산하기 위한 변수
        home_chicken_dist = float("inf")
        # 하나의 치킨집 폐업 시나리오에서 하나의 집에 대해 치킨 거리를 계산하기 위한 반복문
        for k in range(M):
            # 하나의 치킨집 폐업 시나리오에 존재하는 하나의 치킨집 인덱스 쌍 선택
            market_y, market_x = market_combination_idx_ary[i][k]
            dist = abs(market_y - home_y) + abs(market_x - home_x)
            # 집에 대한 기존의 치킨 거리보다 짧은 거리를 구했다면 업데이트
            if dist < home_chicken_dist:
                home_chicken_dist = dist
        # 하나의 집에 대한 치킨 거리를 구했다면
        # 도시의 치킨 거리를 구하기 위해 집에 대한 치킨 거리를 누적합 시킴
        city_chicken_dist += home_chicken_dist
    # 하나의 치킨집 폐업 시나리오에 대해 도시의 치킨 거리를 구했으므로, 이 값을 배열에 기록
    city_chicken_dist_scenario_ary.append(city_chicken_dist)

# 모든 치킨집 폐업 시나리오에 대한 도시의 치킨 거리를 구했으므로, 이 중 최소값을 출력하면 문제 해결
min_chicken_dist = float("inf")
for chicken_dist_scenario in city_chicken_dist_scenario_ary:
    if chicken_dist_scenario < min_chicken_dist:
        min_chicken_dist = chicken_dist_scenario
print(min_chicken_dist)
