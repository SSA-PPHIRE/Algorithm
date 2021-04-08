#백준 1012 유기농 배추 S2
#DFS로 해결, 재귀 깊이를 설정해줘야 함.
#BFS 풀이도 가능, 추후에 진행해볼 예정

#1. 재귀 깊이를 지정해줌 sys.setrecursionlimit(숫자) - 찾아봄
#2. visited 활용

import sys
sys.setrecursionlimit(100000)
sys.stdin =open('1012.txt', 'r')

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def chk(x, y, dis):
    visited[x][y] = dis

    for i in range(4): #4방 탐색
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx <= n-1 and 0 <= yy <= m-1: #배추 밭 범위 벗어나지 않도록
            if arr[xx][yy] == 1 and visited[xx][yy] == 0:
                # arr[xx][yy] == 0  #배추 확인 후, 중복되게 체크하면 안되므로 제거
                chk(xx, yy, dis)


T = int(input())
for _ in range(T):
    m, n, k = map(int, input().split()) #가로, 세로, 배추위치 개수
    arr = [[0] * m for _ in range(n)]  #m x n 행렬리스트 생성
    visited = [[0] * m for _ in range(n)]

    for _ in range(k): # 배추 생성
        y, x = map(int, input().split())  #[x][y]처럼 넣어주려고 y,x로 받음
        arr[x][y] = 1

    cnt = 0  # 필요한 배추 흰지렁이 수

    for r in range(n): #x좌표
        for c in range(m): #y좌표
            if arr[r][c] == 1 and visited[r][c] == 0:
                visited[r][c] == 1 #체크먼저 해주고 진행
                cnt += 1
                chk(r, c, cnt)

    print(cnt)

