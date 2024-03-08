import sys


def merge_sort(ary):
    if len(ary) < 2:
        return ary

    mid = len(ary) // 2
    left = merge_sort(ary[:mid])
    right = merge_sort(ary[mid:])

    l = r = 0
    merged_ary = []
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            merged_ary.append(left[l])
            l += 1
        else:
            merged_ary.append(right[r])
            r += 1
    merged_ary += left[l:]
    merged_ary += right[r:]
    return merged_ary


# round 함수의 오사오입을 해결하기 위해 round 함수를 사용하는 값에 미세한 수를 더해 .5도 올림이 되도록 구현
EPS = 1e-9

n = int(sys.stdin.readline())

if n == 0:
    sys.stdout.write("0")
else:
    score_list = []
    for _ in range(n):
        tmp = int(sys.stdin.readline())
        score_list.append(tmp)
    # 30% 절사평균 진행 시 앞뒤에서 몇 명의 score를 잘라낼지
    del_people_count = round(n * 15 / 100 + EPS)
    # 병합정렬로 score 오름차순 정렬
    sorted_score_list = merge_sort(score_list)

    sum = 0
    length = 0
    for i in range(del_people_count, len(sorted_score_list) - del_people_count):
        sum += sorted_score_list[i]
        length += 1

    sys.stdout.write(str(round(sum / length + EPS)))
