def solution(n):
    answer = n
    m = answer
    cnt_n = 0
    cnt_m = 0

    # n(answer)의 1의 개수 체크하며 이진수로 끝까지 변환
    while answer > 0:
        div = answer // 2
        mod = answer % 2
        answer = div
        if mod == 1:
            cnt_n += 1
    
    answer = m
    
    # 답 찾을때까지 진행
    while True:
        m += 1
        
        # m의 1의 개수 체크하며 이진수로 끝까지 변환
        while m > 0:
            div = m // 2
            mod = m % 2
            m = div
            if mod == 1:
                cnt_m += 1
        # 조건 만족하면 break
        if cnt_n == cnt_m:
            break
        else:
            cnt_m = 0
            m = answer + 1
            answer += 1
    
    return answer + 1
