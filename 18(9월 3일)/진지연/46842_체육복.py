'''
https://programmers.co.kr/learn/courses/30/lessons/42862

1. cloth 리스트 만들기
cloth = [2,0,2,0,2]
2. 체육복 빌려주기
idx = find 0
if left > 2 :
    left -= 1
    idx += 1
elif right > 2 :
    right -= 1
    idx += 1
3. 최종답
answer = [c for c in cloth if c > 0]
'''

def solution(n, lost, reserve):
    # 1. cloth 만들기
    cloth = [1]*(n+2) 
    for r in reserve:
        cloth[r] += 1
    for l in lost:
        cloth[l] -= 1
    
    # 2. cloth 빌려주기
    for c in range(len(cloth)):
        if cloth[c] > 0:
            continue
            
        if cloth[c-1] >= 2:
            cloth[c-1] -= 1
            cloth[c] += 1
        elif cloth[c+1] >= 2:
            cloth[c+1] -= 1
            cloth[c] += 1

    answer = len([c for c in cloth if c > 0]) - 2

    return answer
