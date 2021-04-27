'''
SWEA 2206 벽부수고 이동하
최단거리 : bfs

처음에는 방문체크를 2차원으로 한번만 하고, cnt가 제일 작은 애만 살려두었다.

반례)
S 0 0 0 0
1 1 1 1 0
0 1 1 1 0
0 0 0 0 0
1
T
이라할 때 (3,0)의 0은 ㅣ로 왔을 때만 체크되고 visited = 1로 바꾸면
>로 오면 체크되지 않음. 근데 >로 온 게 답임!

따라서 visited를 이전에 깬 적이 있을 때와 깬 적이 없을 때로 나누어서 체크해주어야 함

방문체크를 3차원으로 해주어야 한다.
'''
from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]

row, col = map(int, input().split())
arr = [[*input()] for i in range(row)]


visited = [[[-1]*2 for j in range(col)] for i in range(row)]        # 왜 -1? 못 찾으면 -1이니까



queue = deque()
queue.append([0,0,0])
visited[0][0][0] = 1

while queue:
    r, c, broke = queue.popleft()


    for i in range(4):
        new_r = r + dr[i]
        new_c = c + dc[i]

        if 0 > new_r or new_r >= row or 0 > new_c or new_c >= col:
            continue
        
        # 스무스한 경우. 0이면 깬적있든 없든!
        if arr[new_r][new_c] == '0' and visited[new_r][new_c][broke] == -1:
            visited[new_r][new_c][broke] = visited[r][c][broke] + 1
            queue.append([new_r, new_c, broke])
        
        # 1이면 깬적 없을 때만 통과. 그리고 이 칸을 지나면 깬 게 되므로, 깬 visited에 기록함
        elif arr[new_r][new_c] == '1' and broke == 0 and visited[new_r][new_c][1] == -1:
            visited[new_r][new_c][1] = visited[r][c][broke] + 1
            queue.append([new_r, new_c, 1])

tmp = [visited[row - 1][col - 1][0], visited[row - 1][col - 1][1]]

if -1 not in tmp:
    print(min(tmp))
else:
    print(max(tmp))

######################################################
[참고] [오답]

from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]

row, col = map(int, input().split())
arr = [[*input()] for i in range(row)]

# arr = [['0', '1', '1', '1'], ['1', '1', '1', '1'], ['1', '1', '1', '1'], ['1', '1', '1', '0']]
# arr = [['0', '1', '0', '0'], ['1', '1', '1', '0'], ['1', '0', '0', '0'], ['0', '0', '0', '0'], ['0', '1', '1', '1'], ['0', '0', '0', '0']]


visited = [[0]*col for i in range(row)]
root_r, root_c, root_cnt, root_broke = 0,0,1,0
ans = -1

queue = deque()
queue.append([root_r, root_c, root_cnt, root_broke])


while queue:
    r, c, cnt, broke = queue.popleft()
    visited[r][c] = 1
    # print(r,c,arr[r][c],cnt,broke,ans)

    # 종료조건
    if r == row-1 and c == col-1:
        ans = cnt
        break


    for i in range(4):
        new_r = r + dr[i]
        new_c = c + dc[i]

        if 0 > new_r or new_r >= row or 0 > new_c or new_c >= col:
            continue

        if visited[new_r][new_c] == 1:
            continue

        if arr[new_r][new_c] == '1' and broke == 0:
            queue.append([new_r, new_c, cnt+1, 1])

        elif arr[new_r][new_c] == '0':
            queue.append([new_r, new_c, cnt+1, broke])

print(ans)
