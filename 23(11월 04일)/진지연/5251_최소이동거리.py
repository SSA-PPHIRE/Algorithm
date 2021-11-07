'''
최소이동거리
1) adj matrix 만들기
2) bfs로 풀기 
-> 8개만 맞음
'''
from collections import deque

t = int(input())
for tc in range(1, t+1):
    n, edge = map(int, input().split())
    arrs = [list(map(int, input().split())) for _ in range(edge)]
    
    weights = [[0]*(n+1) for _ in range(n+1)]
    for arr in arrs:
        s, e, w = arr[0], arr[1], arr[2]
        weights[s][e] = w
        weights[e][s] = w 
    
    ans = float('inf')
    
    q = deque()
    q.append([0,0])
    minimum_cost = [float('inf') for _ in range(n+1)]
    minimum_cost[0] = 0
    
    while q:
        s, total = q.popleft()
        for new_s in range(n+1):
            if weights[s][new_s] == 0:
                continue
            if minimum_cost[new_s] > total + weights[s][new_s]:
                minimum_cost[new_s] = total + weights[s][new_s]
                q.append([new_s, total + weights[s][new_s]])
    
    print(f'#{tc} {minimum_cost[n]}')
    
    
'''
최소이동거리

w가 작은 순으로 정렬하고
사이클이 없으면 추가한다

이 문제는 n개 점을 다 연결하느 문제가 아니라
0번부터 n번깢 이동하느 최소비용을 알아내야 한다.
'''
def find_rep(n):
    while n != rep[n]:
        n = rep[n]
    return n

t = int(input())
for tc in range(1, t+1):
    total, edge = map(int, input().split())
    rep = [i for i in range(total+1)]
    
    arrs = [list(map(int, input().split())) for _ in range(edge)]
    arrs.sort(key=lambda x: x[2], reverse=True)
    
    cnt = 0
    weights = 0
    
    while cnt <= total - 1:
        s,e,w = arrs.pop()
        # print(s,e,find_rep(s), find_rep(e))
        # 사이클이 있으면 건너뛴다
        if find_rep(s) == find_rep(e):
            continue
        # 사이클이 없으면 e를 s 가족에 포함시킨다
        rep[find_rep(e)] = find_rep(s)
        cnt += 1
        weights += w
        # print(find_rep(s), find_rep(e))

    print(f'#{tc} {w}')
