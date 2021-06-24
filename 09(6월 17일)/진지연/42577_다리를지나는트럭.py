# https://programmers.co.kr/learn/courses/30/lessons/42577/solution_groups?language=python3&type=my

from collections import deque

def solution(b_lgt, b_w, trucks):
    b = deque()
    cnt = 0
    b.append([trucks.pop(0),0])

    while b:
        cnt += 1
        if [0, 0] in b:
            b.remove([0, 0])

        # cnt를 증가시키고, 기준을 초과하면 0으로 대체한다
        for i in range(len(b)):
            b[i][1] += 1
            if b[i][1] >= b_lgt:
                b[i] = [0,0]

        # 합이 b_w 이하이면 더해준다
        if trucks:
            if sum(map(lambda x:x[0], b)) + trucks[0] <= b_w:
                b.append([trucks.pop(0),0])

    return cnt
