#백준 10026 적록색약 G5
'''
빨,초 구별   /   빨, 초 동일하게
'''
#오랜만의 DFS or BFS
#DFS보다 bfs가 더 적절하다 판단.
#시간을 고려할 때, visited 쓰는게 좋음
#python3가 pypy3보다 시간이 더 적게 나옴.

from collections import deque

import sys
sys.stdin = open('text/10026.txt', 'r')

dx = [1,-1,0,0]  #동 서 남 북
dy = [0,0,1,-1]

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(input().rstrip()))

visited = [[0] * n for _ in range(n)] # 방문 여부 체크용


def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    while queue:
        pos = queue.popleft()   # (x,y)
        for i in range(4):  #4방향 탐색
            xx, yy = pos[0] + dx[i], pos[1] + dy[i]
            if 0<= xx < n and 0 <= yy < n:  #범위 안이고
                if visited[xx][yy] == 0 and arr[x][y] == arr[xx][yy]: #방문 하지 않았고, 같은 값을 가진다면
                    visited[xx][yy] = visited[x][y] # 이동한 지점도 방문했다고 체크해주고 큐에 넣어주자
                    queue.append((xx, yy))

res1 = 0 # 정상인

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            res1 += 1
            bfs(i,j)

res2 = 0  #색맹

for i in range(n):  # visited 초기화 해줘야 함. (처음에는 2개 만들어주려 했으나, bfs 함수 하나로 처리하기위해 한개만들고 초기화)
    for j in range(n):  #for문 돌리는 김에 G와 R도 동일하게 처리를 해줌.
        visited[i][j] = 0
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            res2 += 1
            bfs(i,j)

print(res1, res2)


