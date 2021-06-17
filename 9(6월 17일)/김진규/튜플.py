def solution(s):
    answer = []
    lst = s.split('{')
    res = []
    tup = []
    for i in range(len(lst)):
        lst[i] = lst[i].strip('},')

    for i in range(len(lst)):
        if lst[i] != '':
            tmp = set(map(int, lst[i].split(',')))
            res.append(tmp)
    res.sort(key=lambda x:len(x))

    tup.append(list(res[0])[0])
    for i in range(1, len(res)):
        tup.append((res[i] - res[i-1]).pop())

    return tup
