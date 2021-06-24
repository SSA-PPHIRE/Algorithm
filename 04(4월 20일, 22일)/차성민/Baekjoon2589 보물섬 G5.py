#벡준 2589 보물섬 G5
#BFS문제, 가장 거리가 긴 시간 출력
#파이썬3 - 시간초과, PYPY3 - 통과 (효율적이지 않았기 때문)

from collections import deque
import sys
sys.stdin = open('text/2589.txt', 'r')

# L을 만날 때 마다 진행해주면서 가장 긴 시간 구함
# visited를 활용.
# 큐에 지난주에 이어서 좌표 값 이외에 거리를 넣어줌
# 보다 효율적인 방법을 구하고 싶음 (모든 L좌표에서가 아닌 끝 좌표 값에서만 BFS하도록?)

#사방향
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def BFS(x, y):
    q = deque()
    q.append((x, y, 0))  # 좌표 값과 현재 거리 값을 같이 큐에 넣어줌
    dist = 0
    visited[x][y] = 1 #방문 체크

    while q:
        xx, yy, d = q.popleft()

        for i in range(4):
            x = xx + dx[i]
            y = yy + dy[i]

            if 0 <= x < c and 0<= y < r: #경계선 안이고,
                if treasure[x][y] == 'L' and visited[x][y] == 0: # L이면서 방문하지 않았다면 거리 1증가시키고 큐에 추가
                    q.append((x, y, d+1))
                    visited[x][y] = 1
                    dist = d+1
    return dist # (x,y)좌표에서의 최대 길이 구한 다음에 반환

c, r = map(int, input().split()) #세로, 가로
treasure = []
res = 0
for _ in range(c):
    treasure.append(list(input()))

for i in range(c):
    for j in range(r):
        if treasure[i][j] == 'L':
            visited = [[0] * r for _ in range(c)] #visited 활용, 매 회차별로  초기화를 해줌
            res = max(res, BFS(i, j))

print(res)

