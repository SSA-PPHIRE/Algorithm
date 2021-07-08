def solution(priorities, location):
    id_pri = []
    max_pri = 0
    cnt = 0
    for idx, pri in enumerate(priorities):
        id_pri.append((idx, pri))
        if pri >= max_pri:
            max_pri = pri
    while True:
        if id_pri[0][1] == max_pri:
            idx, pri = id_pri.pop(0)
            cnt += 1
            if idx == location:
                return cnt
            max_pri = max(id_pri, key=lambda x:x[1])[1]
        else:
            id_pri.append(id_pri.pop(0))
