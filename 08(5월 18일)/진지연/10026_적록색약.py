'''
처음에 dfs로 풀었는데 런타임에러가 났다..
검색해보니 다드 bfs로 풀길래 풀었다.
'''

from collections import deque

n = int(input())
arr = [[*input()] for _ in range(n)]
delta = [[-1,0], [0,1], [1,0], [0,-1]]
visited = [[0]*n for _ in range(n)]
q = deque()

def bfs(r,c):
    q.append([r,c])
    visited[r][c] = 0
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + delta[i][0]
            nc = c + delta[i][1]

            if 0 <= nr < n and 0 <= nc < n:
                if arr[r][c] == arr[nr][nc] and visited[nr][nc] == 0:
                    q.append([nr, nc])
                    visited[nr][nc] = 1

cnt = 0
for r in range(n):
    for c in range(n):
        if visited[r][c] == 0:
            bfs(r,c)
            cnt += 1
print(cnt, end=' ')

for r in range(n):
    for c in range(n):
        if arr[r][c] == 'R':
            arr[r][c] = 'G'

visited = [[0]*n for _ in range(n)]
cnt = 0
for r in range(n):
    for c in range(n):
        if visited[r][c] == 0:
            bfs(r,c)
            cnt += 1
print(cnt)
