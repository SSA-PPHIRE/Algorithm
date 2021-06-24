def solution(progresses, speeds):
    day_lst = []
    res = []
    for i in range(len(progresses)):
        n = 0
        while progresses[i] + n * speeds[i] < 100:
            n += 1
        day_lst.append(n)
    
    
    while day_lst:
        cnt = 0
        first = day_lst[0]
        while day_lst:
            if day_lst[0] <= first:
                cnt += 1
                day_lst.pop(0)
            else:
                break
        res.append(cnt)
    
    return res
