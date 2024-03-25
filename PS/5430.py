import sys
from collections import deque


def return_ary(string):
    start_idx = 0
    queue = deque()
    for i in range(len(string)):
        if string[i] == "[":
            start_idx += 1
            continue
        if string[i] == ",":
            queue.append(int(string[start_idx:i]))
            start_idx = i + 1
            continue
        if string[i] == "]":
            if i == 1:
                return queue
            queue.append(int(string[start_idx:i]))
            break
    return queue


def function_R(queue):
    new_queue = deque()
    while queue:
        new_queue.append(queue.pop())
    return new_queue


def print_func(queue):
    if len(queue) == 0:
        sys.stdout.write("[]" + "\n")
        return
    sys.stdout.write("[")
    for i in range(len(queue) - 1):
        sys.stdout.write(str(queue[i]) + ",")
    sys.stdout.write(str(queue[len(queue) - 1]) + "]\n")


T = int(sys.stdin.readline())

for _ in range(T):
    functions = sys.stdin.readline().rstrip()
    _ = sys.stdin.readline().rstrip()
    string = sys.stdin.readline().rstrip()
    num_queue = return_ary(string)  # 문자열을 실제 정수 배열로 변환해서 반환
    finish_print_flag = True

    # R이 홀수번 존재할때만 R을 수행하고, R과 R 사이 D는 R이 홀수갠지 짝수갠지에 따라 다르게 처리
    r_cnt = 0
    for function in functions:
        if function == "R":
            r_cnt += 1
            continue
        elif function == "D":
            if len(num_queue) == 0:
                sys.stdout.write("error\n")
                finish_print_flag = False
                break
            else:
                if r_cnt % 2 == 0:
                    num_queue.popleft()
                else:
                    num_queue.pop()

    if r_cnt % 2 == 1:
        num_queue = function_R(num_queue)

    if finish_print_flag:
        print_func(num_queue)
