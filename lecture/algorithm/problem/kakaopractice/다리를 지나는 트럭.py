from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights.sort(reverse=True)
    stack_weight = deque()
    stack_time = deque()
    while True:
        if len(truck_weights) == 0 and len(stack_weight) == 0 and len(stack_time) == 0:
            return answer
        answer += 1
        for _ in range(len(stack_time)):
            stack_time[_] += 1
        if len(stack_time) != 0 and stack_time[0] == bridge_length:
            stack_time.popleft()
            stack_weight.popleft()

        if len(truck_weights) != 0:
            if sum(stack_weight) + truck_weights[0] <= weight:
                a = truck_weights.pop(0)
                stack_weight.append(a)
                stack_time.append(0)