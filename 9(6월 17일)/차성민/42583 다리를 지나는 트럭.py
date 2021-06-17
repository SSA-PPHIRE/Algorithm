from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque([0] * bridge_length) # 올라갈 수 있는 트럭 수 만큼의 크기로 큐 생성(트럭이 시간에 따라 지날 때 반영을 해주기 위해)
    current_weight = 0 # 현재까지의 무게 확인을 위해 생성해줌 (두개이상의 트럭도 같이 보낼 수 있게)
    truck_weights.reverse()
    '''
        현재까지의 무게 + 다음 트럭의 무게가 한계 무게보다 큰지 확인
        트럭을 올리는 방법만을 고려하여 시간을 먼저 구하고, 
        트럭이 모두 없어진 다음에 answer에 다리에 올라갈 수 있는 트럭 수 만큼 더해줌.
    '''

    while truck_weights: #트럭이 없어질 때 까지
        current_weight -= queue.popleft()

        if current_weight + truck_weights[-1] > weight:
            queue.append(0)

        else:
            current_truck = truck_weights.pop()
            queue.append(current_truck)
            current_weight += current_truck
        answer += 1

    
    answer += bridge_length

    return answer
