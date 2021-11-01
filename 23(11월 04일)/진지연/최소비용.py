'''
제한시간 초과
dfs 재귀함수로 구현할 때 어떻게 방문체크를 할까?
-> 방문체크가 의미가 있나? 
    5 5
    0 10
    12 11
    에서 (0,0) -> (2,0)으로 갈 때
    (1,0)을 거쳐 가는 경우 : 14
    (1,0)을 거치지 않고 가는 경우 : 11임

'''

def dfs(r,c,oil):
    global n, ans
    # 조기종료
    if ans < oil:
        return
    # 종료조건
    if r == n-1 and c == n-1:
        ans = oil
        return
    for i in range(4):
        new_r = r + dirs[i][0]
        new_c = c + dirs[i][1]
        if new_r < 0 or new_r >= n or new_c < 0 or new_c >= n:
            continue
        diff = max(arr[new_r][new_c] - arr[r][c], 0)
        dfs(new_r, new_c, oil + diff + 1)


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = float('inf')
    oil = 0
    dirs = [[0,1], [1,0], [0,-1], [-1,0]]
    dfs(0,0,0)
    print(f"#{tc} {ans}")

    
'''
bfs로.
더 좋은 값을 찾으면 다시 탐색한다
'''

from collections import deque
delta = [[-1,0], [0,1], [1,0], [0,-1]]

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    visited = [[float('inf')]*n for _ in range(n)]
    visited[0][0] = 0

    q = deque([[0,0]])
    while q:
        r, c = q.popleft()

        for i in range(4):

            new_r = r + delta[i][0]
            new_c = c + delta[i][1]

            if new_r < 0 or new_r >= n or new_c < 0 or new_c >= n:
                continue
            diff = max(arr[new_r][new_c]-arr[r][c], 0)
            
            # 더 좋은 값을 찾으면 new_r, new_c를 다시 탐색한다
            if visited[new_r][new_c] > visited[r][c] + 1 + diff:
                visited[new_r][new_c] = visited[r][c] + 1 + diff
                q.append([new_r, new_c])


    print(f'#{tc} {visited[n-1][n-1]}')
