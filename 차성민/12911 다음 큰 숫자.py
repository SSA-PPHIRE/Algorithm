def solution(n):
    answer = n
    m = answer
    cnt_n = 0
    cnt_m = 0

    while answer > 0:
        div = answer // 2
        mod = answer % 2
        answer = div
        if mod == 1:
            cnt_n += 1
    
    answer = m
    
    while True:
        m += 1
        while m > 0:
            div = m // 2
            mod = m % 2
            m = div
            if mod == 1:
                cnt_m += 1
        if cnt_n == cnt_m:
            break
        else:
            cnt_m = 0
            m = answer + 1
            answer += 1
    
    return answer + 1
