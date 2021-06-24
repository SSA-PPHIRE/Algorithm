from collections import deque

def solution(bridge_length, weight, truck_weights):
    s = deque()
    truck_weights = deque(truck_weights)
    time = 0
    now_weight = 0
    while truck_weights or s:
        time += 1
        if s:
            if s[0][1]+bridge_length == time:
                y = s.popleft()
                now_weight -= y[0]
        if truck_weights:
            if weight < now_weight+truck_weights[0]:
                continue
            x = truck_weights.popleft()
            s.append((x, time))
            now_weight += x
        
    
    return time
