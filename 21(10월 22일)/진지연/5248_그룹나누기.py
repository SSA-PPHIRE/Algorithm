'''
최종 목적 : 몇 개의 조가 만들어지는가
rep = [0,1,2,3,4,5]
replace(1,2) : rep[1] <= rep[2]
'''

def find_rep(n):
    while n != rep[n]:
        n = rep[n] 
    return n

def replace_rep(a, b):
    rep[find_rep(a)] = rep[find_rep(b)]

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    rep = [i for i in range(n+1)]
    pairs = list(map(int, input().split()))
    for i in range(m):
        a = pairs[2*i]
        b = pairs[2*i+1]
        rep[find_rep(a)] = rep[find_rep(b)]
    cnt = -1
    for i in range(n+1):
        if i == rep[i]:
            cnt += 1
    print(f'#{tc} {cnt}')
 
