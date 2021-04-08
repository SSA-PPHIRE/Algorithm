# DFS를 재귀 함수로 구현했을 때 최대 재귀 횟수 초과
################################
# 이것을 사용하여 최대 재귀 횟수를 늘릴시 통과
import sys
sys.setrecursionlimit(10 ** 4)
#################################
def check(a, b):
    # 4방향 탐색
    for k in range(4):
        c = a + d_a[k]
        d = b + d_b[k]
        # 배추가 존재하고 방문하지 않았다면 방문표시를 하고 다시 탐색
        if 0 <= c < N and 0 <= d < M and baechu[c][d] == 1 and visited[c][d] != 1:
            visited[c][d] = 1
            check(c, d)
###################################
# 스택을 이용한 DFS
def check(a, b):
    s = [(a,b)]
    while s:
        x, y = s.pop()
        for k in range(4):
            c = x + d_a[k]
            d = y + d_b[k]
            if 0 <= c < N and 0 <= d < M and baechu[c][d] == 1 and visited[c][d] != 1:
                visited[c][d] = 1
                s.append((c,d))


T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    # 배추 위치
    baechu = [[0] * M for _ in range(N)]
    # 방문 여부 확인용 배열
    visited = [[0] * M for _ in range(N)]
    # 총 갯수
    cnt = 0
    # delta list
    d_a = [1, 0, -1, 0]
    d_b = [0, 1, 0, -1]
    # 배추의 위치를 저장
    for i in range(K):
        x, y = map(int, input().split())
        baechu[y][x] = 1
    # 배추 배열을 처음부터 끝까지 탐색
    for i in range(N):
        for j in range(M):
            # 만약 배추가 존재하고 방문하지 않았다면 방문표시를 하고 check 실행 및 cnt 증가
            if baechu[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] = 1
                check(i, j)
                cnt += 1
    print(cnt)
