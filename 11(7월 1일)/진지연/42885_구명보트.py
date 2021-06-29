# 계약서 읽듯이 문제를 읽자
# 보트엔 '최대 두명'만 탈 수 있다는 제약조건이 있었다


def solution(people, limit):
    answer = len(people) # 보트 수 초기값 사람 수 만큼
    light_idx, heavy_idx = 0, len(people)-1
    people.sort() # 정렬
    
    while light_idx <  heavy_idx:
        # 가벼운 + 무거운 사람 같이 탈 수 있을 경우
        # 짝지어지면 보트 수 하나 빼기
        if people[light_idx] + people[heavy_idx] <= limit :
            answer -= 1
            light_idx +=1
            heavy_idx -=1
        
        # 같이 못탈 경우 무거운 사람 혼자 보냄
        else :
             heavy_idx -=1
    
    return answer
