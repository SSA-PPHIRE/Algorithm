'''
computers[i][j] == 1이면
i의 rep를 rep(j)로 대체한다
'''

def rep(n, root):
    while n != root[n]:
        n = root[n]
    return n

def solution(n, computers):
    root = [i for i in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if computers[i][j] == 1:
                root[rep(i, root)] = rep(j, root)
    cnt = 0
    for i in range(n):
        if i == root[i]:
            cnt += 1
    
    return cnt
