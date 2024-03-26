import sys

# 최소 힙을 구현하기 위한 배열
heap = []
# 정답 값을 저장하기 위한 배열
res_ary = []


# 최소 힙에 Push하는 함수
def heap_push(item):
    heap.append(item)  # 우선은 힙의 맨 뒤에다 push하려는 값을 삽입
    # 만약 힙의 크기가 1이라면 (원래는 공백인 힙이였다면)
    # 최소 힙을 유지하기 위한 스왑 과정이 필요 없다. return으로 아래 과정 생략
    if len(heap) == 1:
        return

    # cur_idx = 삽입한 item의 index다.
    # while문에서 item이 본인의 부모보다 작다면 -> 부모와 위치를 스왑해서 최소 힙을 유지한다
    cur_idx = len(heap) - 1
    # 0보다 크다는 조건 : root 까지 올라가면, 더 이상 비교할 부모가 없으므로 반복문을 종료해야 함
    # heap[cur_idx] < heap[(cur_idx - 1) // 2] : item이 item의 부모보다 작은 경우 (스왑이 필요한 경우)

    # cur_idx의 부모 idx = cur_idx // 2 ?
    # <- 이렇게 처리하면, left child index는 parent index로 변하겠지만, right child index는 parent index가 아닌 값으로 변해 로직이 꼬임!!
    # Ex : 0의 자식 1, 2에 대해 ( 1 // 2 == 0 but 2 // 2 == 1)
    # 만약 // 2를 사용하고 싶다면, pop에서 * 2 + 1이 아닌, * 2를 사용해야 한다.
    while cur_idx > 0 and heap[cur_idx] < heap[(cur_idx - 1) // 2]:
        tmp = heap[cur_idx]
        heap[cur_idx] = heap[(cur_idx - 1) // 2]
        heap[(cur_idx - 1) // 2] = tmp
        # 스왑을 진행한 뒤, cur_idx를 부모 idx로 변경해준다. (부모랑 스왑했으니까 item 위치는 당연히 변한다)
        cur_idx = (cur_idx - 1) // 2


# 최소 힙에서 root를 Pop하는 함수
def heap_pop():
    # 만약 heap이 비어있다면 0 반환 (이는 문제의 조건임)
    if len(heap) == 0:
        return 0
    # 만약 heap의 크기가 1이라면, 반환하고 나서 스왑 과정을 거칠 필요가 없다.
    if len(heap) == 1:
        return heap.pop()

    # heap의 크기가 2 이상이라면, 아래 메커니즘에 따라 pop을 수행해야 한다.
    # v는 반환할 값, root값이다. 이를 잠깐 복사해둔다
    v = heap[0]
    # root자리 값을 버리고, 가장 마지막에 들어온 값을 root 자리로 이동시킨다.
    heap[0] = heap.pop()
    # cur_idx = 가장 마지막에 들어온 값이 root로 이동했으므로, 이 가장 마지막에 들어온 값 때문에 최소 힙이 깨진다.
    # 이를 바로잡기 위해 cur_idx = 0으로 배치하고, 이 root로 이동된 값을 아래로 내려보낼 것이다.
    cur_idx = 0
    # child_idx = 앞으로 cur_idx의 왼쪽 자식 노드의 인덱스로 고정한다.
    child_idx = 1

    # 접근하려는 인덱스가 heap의 범위를 벗어나지 않도록 조건문을 달아주고
    while child_idx < len(heap):
        # 형제 노드의 index (cur의 오른쪽 자식 노드의 index)를 계산해준다.
        sibling_idx = child_idx + 1
        # cur의 오른쪽 자식 노드의 index 범위도 heap의 안에 들어있고, cur의 왼쪽 자식 노드보다 cur의 오른쪽 자식 노드가 더 작다면
        # 오른쪽 자식 노드의 index를 child_idx에 적용하고, 아래에서 이 child_idx와 교환할지 여부를 고려한다.
        # 즉 아래 if문은 오른쪽 자식과 교환할지, 왼쪽 자식과 교환할지 방향을 정해주는 if문이다.
        # (최소 힙에서 pop을 수행하게 될 때, 부모 노드가 자식노드 둘 다보다 큰 경우, 자식 노드 중 작은 자식과 교환하게 된다)
        # (사실 당연한것인 이유가 최소 힙은 위로 올라갈수록 값이 작아져야 하므로, 자식들 중 가장 작은 자식과 교환하는게 당연하다)
        if sibling_idx < len(heap) and heap[sibling_idx] < heap[child_idx]:
            child_idx = sibling_idx
        # 아래 if문은 부모와 자식 간 크기를 비교하는 부분이다.
        # 위쪽 if문에서 자식 간의 크기는 비교가 끝났고, 자식들 중 가장 작은 값보다 부모가 크다면, 이 자식과 부모를 스왑하면 될 뿐이다.
        if heap[cur_idx] > heap[child_idx]:
            tmp = heap[cur_idx]
            heap[cur_idx] = heap[child_idx]
            heap[child_idx] = tmp
            # 자식과 부모를 교환했으면, cur_idx(root로 옮겨진, 마지막에 삽입된 값의 index) 값을 스왑한 자식 노드의 원래 index로 수정해주고
            # 자식의 index는 본인 * 2로 바꿔준다. (이는 이진트리를 배열로 표현하는 과정에서 나온다)
            cur_idx = child_idx
            child_idx = cur_idx * 2 + 1
        # 이 else문이 없어서 계속 시간 초과가 발생했었다.
        # 사실 생각해보면, 자식 간 크기 비교는 마쳤는데, 가장 작은 자식(child_idx)보다 부모(cur_idx)가 더 작게 되면, 여기서 스왑을 마쳐야 한다. (버블링이라고 했나 이걸)
        # 근데 이 break가 없으면, 스왑을 하진 않는데, 무한으로 while문이 작동하게 된다. 이래서 시간초과가 발생했던 것이다!!
        else:
            break
    return v


N = int(sys.stdin.readline())
for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        v = heap_pop()
        res_ary.append(v)
    else:
        heap_push(num)
for res in res_ary:
    sys.stdout.write(str(res) + "\n")
