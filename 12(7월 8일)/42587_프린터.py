'''
2132
1322
3221

list.pop(), .append()는 비효율적
원형큐라 생각 + pointer를 사용하자

'''

def solution(priorities, location):
    pointer = 0
    cnt = 0
    n = len(priorities)
    while True:
        if priorities[location] == 0:
            return cnt
        if priorities[pointer] == max(priorities):
            priorities[pointer] = 0
            cnt += 1
        else:
            pointer = (pointer + 1) % n

    return answer
