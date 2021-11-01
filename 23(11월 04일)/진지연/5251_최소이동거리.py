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
