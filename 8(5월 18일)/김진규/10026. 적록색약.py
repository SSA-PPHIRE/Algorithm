from collections import deque
from copy import deepcopy


# bfs
def check(r, c, v, arr):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    v[r][c] = 1
    color = arr[r][c]
    q = deque()
    q.append((r, c))
    while q:
        x, y = q.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < N and 0 <= yy < N and arr[xx][yy] == color and v[xx][yy] == 0:
                v[xx][yy] = 1
                q.append((xx, yy))


N = int(input())
nrg_arr = [list(input()) for _ in range(N)]  # 적록 색약이 아닌 사람들
rg_arr = deepcopy(nrg_arr)  # 적록 색약인 사람들
for i in range(N):
    for j in range(N):
        if rg_arr[i][j] == 'R':
            rg_arr[i][j] = 'G'

v1 = [[0]*N for _ in range(N)]  # 적록 색약이 아닌 사람 방문체크
v2 = [[0]*N for _ in range(N)]  # 적록 색약인 사람 방문체크
cnt1, cnt2 = 0, 0  # 각각의 구역의 수
for i in range(N):
    for j in range(N):
        # 방문하지 않은 구역일 때
        # 구역 전체를 bfs하여 방문체크 후
        # 구역의 수 + 1
        if v1[i][j] == 0:
            check(i, j, v1, nrg_arr)
            cnt1 += 1
        if v2[i][j] == 0:
            check(i, j, v2, rg_arr)
            cnt2 += 1

print(cnt1, cnt2)
