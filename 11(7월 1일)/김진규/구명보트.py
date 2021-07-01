# 그리디라길래 그리디로 풀었슴당

def solution(people, limit):
    # 사람들 정렬    
    people.sort()
    # 보트 수
    cnt = 0
    # 시작과 끝
    s, e = 0, len(people)-1
    
    while s <= e:
        # 제일 무거운 사람과 가벼운 사람을 더해서 한계보다 낮다면
        # 시작과 끝 모두 하나씩 이동하고 보트 수 증가
        if people[s] + people[e] <= limit:
            s += 1
            e -= 1
            cnt += 1
        # 그렇지 않다면 끝만 이동 보트 수 증가
        else:
            e -= 1
            cnt += 1
    
    answer = cnt
    return answer
