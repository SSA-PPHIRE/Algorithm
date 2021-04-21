# 그냥 bfs 한다음 나온 거리중 최댓값을 구하면 됨
# 나중에 주석 추가 예정

from collections import deque


def bfs(r, c):
    visited[r][c] = 0
    q = [(r, c, 0)]
    q = deque(q)
    while q:
        x, y, dist = q.popleft()
        distance.add(dist)
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < N and 0 <= yy < M and arr[xx][yy] == 'L' and visited[xx][yy] == -1:
                visited[xx][yy] = dist + 1
                q.append((xx, yy, dist + 1))


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
distance = set()

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            visited = [[-1] * M for _ in range(N)]
            bfs(i, j)

print(max(distance))
