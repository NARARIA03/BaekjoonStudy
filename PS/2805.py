import sys


# 나무들을 mid_h 높이에서 자르면 얻을 수 있는 나무의 총합을 계산
# 나무의 총합이 M보다 작다면 "down" 반환 (나무를 더 베어야 하므로)
# 나무의 총합이 M보다 크거나 같다면 "up" 반환 (나무를 덜 베어도 되므로)
def cut_tree(mid_h):
    tree_h = 0
    for tree in tree_ary:
        # 이 if문 매우 중요!! 음수의 영역을 까먹지 말자...
        # if문 없이 진행하면 나무보다 자르는 높이가 더 높은 경우 자른 나무의 높이가 음수가 되버린다
        if tree <= mid_h:
            continue
        tree_h += tree - mid_h
    if tree_h < M:
        return "down"
    elif tree_h >= M:
        return "up"


# N = 나무의 수
# M = 상근이가 필요한 나무 길이
N, M = map(int, sys.stdin.readline().split())
tree_ary = list(map(int, sys.stdin.readline().split()))

# 먼가 느낌이 이진탐색임
max_h = max(tree_ary)
min_h = 0

# 이진탐색은 기본적으로 l < r 인 동안 반복하게 조건 설정
while min_h < max_h:
    mid_h = (max_h + min_h) // 2
    flag = cut_tree(mid_h)

    # mid에서 잘라보니까, 내려야 한다고 함
    if flag == "down":
        # 1 내려서 잘라봄
        flag2 = cut_tree(mid_h - 1)
        # 1 내려서 잘라보니까 올려도 된다고 함 -> 1 내려서 자른 지점이 곧 우리가 원하는 지점임
        if flag2 == "up":
            mid_h -= 1  # mid_h에 1 뺀거 반영하고 반복문 탈출
            break
        # 경계 지점에 도달하지 못했으면, 이진 탐색 방식대로 r 값을 m으로 세팅해줌
        max_h = mid_h

    # mid에서 잘라보니까 올려도 된다고 함
    elif flag == "up":
        # 1 올려서 잘라봄
        flag2 = cut_tree(mid_h + 1)
        # 1 올려서 잘라보니까 내려야 한다고 함 -> 1 올리기 전 지점이 곧 우리가 원하는 지점임
        if flag2 == "down":
            break  # 반복문 탈출
        # 경계 지점에 도달하지 못했으면, 이진 탐색 방식대로 l 값을 m으로 세팅해줌
        min_h = mid_h

# 정답 출력
print(mid_h)
