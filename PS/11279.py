import sys
from collections import deque

maximum_heap = deque()
res_ary = []


def maximum_heap_push(e):
    if len(maximum_heap) == 0:
        maximum_heap.append(e)
        return

    maximum_heap.append(e)
    e_idx = len(maximum_heap) - 1

    # Root index를 0으로 삼은 트리에서 부모 노드 index는 (e_idx - 1) // 2와 같이 접근하자!
    while e_idx > 0 and maximum_heap[(e_idx - 1) // 2] < maximum_heap[e_idx]:
        tmp = maximum_heap[(e_idx - 1) // 2]
        maximum_heap[(e_idx - 1) // 2] = maximum_heap[e_idx]
        maximum_heap[e_idx] = tmp
        e_idx = (e_idx - 1) // 2
    return


def maximum_heap_pop():
    if len(maximum_heap) == 0:
        return 0
    if len(maximum_heap) == 1:
        return maximum_heap.pop()

    return_v = maximum_heap[0]
    maximum_heap[0] = maximum_heap.pop()

    parent_idx = 0
    child_idx = 1
    while child_idx < len(maximum_heap):
        siblig_idx = child_idx + 1
        if (
            siblig_idx < len(maximum_heap)
            and maximum_heap[siblig_idx] > maximum_heap[child_idx]
        ):
            child_idx = siblig_idx

        # 예전에 최소 힙 구현할때 실수했던 부분 또 함, 이 if문에 대한 else break가 필요하다.
        if maximum_heap[parent_idx] < maximum_heap[child_idx]:
            tmp = maximum_heap[child_idx]
            maximum_heap[child_idx] = maximum_heap[parent_idx]
            maximum_heap[parent_idx] = tmp
            parent_idx = child_idx
            child_idx = parent_idx * 2 + 1
        else:
            break
    return return_v


N = int(sys.stdin.readline())

for _ in range(N):
    q = int(sys.stdin.readline())
    if q == 0:
        answer = maximum_heap_pop()
        res_ary.append(answer)
    else:
        maximum_heap_push(q)

for res in res_ary:
    sys.stdout.write(str(res) + "\n")
