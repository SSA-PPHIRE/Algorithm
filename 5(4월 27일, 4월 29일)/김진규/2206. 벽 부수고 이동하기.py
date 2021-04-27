from collections import deque

# 풀던 방법에서 배열을 하나 더 추가해서 풀었다
# 나머지 원리는 다른 분들이 푼 것과 동일!
# 중요한 것은 방문체크 하는 배열이 2개인 것
def bfs(x, y):
    q = deque()
    q.append((x, y, 1, 1))
    v[x][y] = 1
    v1[x][y] = 1
    while q:
        nx, ny, dist, flag = q.popleft()
        if nx == N - 1 and ny == M - 1:
            if flag:
                return v[nx][ny]
            else:
                return v1[nx][ny]

        for i in range(4):
            xx = nx + dx[i]
            yy = ny + dy[i]

            if 0 <= xx < N and 0 <= yy < M:
                if v[xx][yy] == 0 and flag == 1 and map_arr[xx][yy] == '0':
                    q.append((xx, yy, dist+1, flag))
                    v[xx][yy] = dist+1
                if v1[xx][yy] == 0 and flag == 0 and map_arr[xx][yy] == '0':
                    q.append((xx, yy, dist + 1, flag))
                    v1[xx][yy] = dist + 1
            if 0 <= xx < N and 0 <= yy < M and v1[xx][yy] == 0 and flag == 1 and map_arr[xx][yy] == '1':
                q.append((xx, yy, dist+1, flag-1))
                v1[xx][yy] = dist+1
    return -1

N, M = map(int, input().split())
map_arr = [list(input()) for _ in range(N)]
v = [[0]*M for i in range(N)]
v1 = [[0]*M for i in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
print(bfs(0, 0))
