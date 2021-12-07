'''
시간초과 뜸
permutations 부분을 수기로 작성해보자
'''
from itertools import permutations

t = int(input())
for tc in range(1, t+1):
    N, L, R = map(int, input().split())
    ans = 0
    pool = [i for i in range(1, N+1)]

    def countLook(lst, limit):
        mx = 0
        tmp = 0
        for l in lst:
            if l > mx:
                mx = l
                tmp += 1
        return tmp == limit

    for i in permutations(pool):
        if countLook(i, L) & countLook(i[::-1], R):
            ans += 1
    print(f"#{tc} {ans}")
    
    
'''
시간초과 뜸
'''

def countLook(lst, limit):
    mx = 0
    tmp = 0
    for l in lst:
        if tmp > limit:
            return (False, 0)
        if l > mx:
            mx = l
            tmp += 1
    return (True, tmp)


def p(lst, N, L, R):
    global cnt
    print(lst)
    if not countLook(lst, L)[0]:
        return


    if len(lst) == N:
        if countLook(lst, L)[1] == L and countLook(lst[::-1], R)[1] == R:
            cnt += 1
        return

    if len(lst) == N:
        return

    for i in range(1, N+1):
        if i not in lst:
            lst.append(i)
            p(lst, N, L, R)
            lst.remove(i)

t = int(input())
for tc in range(1, t+1):
    N, L, R = map(int, input().split())
    cnt = 0
    p([], N, L, R)
    print(f"#{tc} {cnt}")
