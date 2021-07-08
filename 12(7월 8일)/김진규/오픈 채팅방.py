def solution(record):
    name_dict = {}
    come_lst = []
    res = []
    for i in range(len(record)):
        lst = record[i].split()
        if lst[0] == 'Enter' or lst[0] == 'Change':
            state, user_id, name = lst
            name_dict[user_id] = name
            if state == 'Enter':
                come_lst.append((state, user_id))

        else:
            state, user_id = lst
            come_lst.append((state, user_id))

    for i in range(len(come_lst)):
        state, user_id = come_lst.pop(0)
        if state == 'Enter':
            res.append("{}님이 들어왔습니다.".format(name_dict[user_id]))
        else:
            res.append("{}님이 나갔습니다.".format(name_dict[user_id]))
    
    
    return res
