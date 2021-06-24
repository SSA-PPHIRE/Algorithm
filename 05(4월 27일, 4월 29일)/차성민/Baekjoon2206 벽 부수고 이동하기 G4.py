#백준 2206 벽 부수고 이동하기 G4
# 실패
#시작점이 (0,0)이 아닌 (1,1)
# 최단경로 - BFS
# 불가능시 -1 출력
# Key : 벽을 부수고 갈 수 있다는 점  = > visited를 3차원 배열로 만들어 주자
# 다양한 반례를 생각해봐야 함을 많이 느낄 수 있었음.

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split(" "))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 방문 확인용 배열
visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(2)]
# 인풋으로 받을 배열
arr = []

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().strip())))

queue = deque()

# 시작점이 완료점일 경우 예외처리
if n == 1 and m == 1 and arr[0][0] == 0:
    print(1)

else:
    visited[0][0][0] = 1
    queue.append([0, 0, 0])

    flag = 0
    while queue:
        x, y, z = queue.popleft()

        for i in range(4):
            ndr = x + dx[i]
            ndc = y + dy[i]

            # 범위안에 들어옴
            if 0 <= ndr < n and 0 <= ndc < m and visited[z][ndr][ndc] == 0:

                c = 0
                # 벽을 만났는데 아직 벽을 안뚫어봄
                if arr[ndr][ndc] == 1 and z == 0:
                    visited[1][ndr][ndc] = visited[0][x][y] + 1
                    queue.append([ndr, ndc, 1])
                    c = 1

                # 벽 안만남 (길을 만난 경우)
                elif arr[ndr][ndc] == 0:
                    visited[z][ndr][ndc] = visited[z][x][y] + 1
                    queue.append([ndr, ndc, z])

                # 도착한 경우
                if ndr == n - 1 and ndc == m - 1:
                    print(visited[z][ndr][ndc])
                    flag = 1
                    break

        if flag == 1:
            break

    if flag == 0:
        print(-1)

''' heapq를 이용한 풀이법
import sys
import heapq

height, width = map(int, sys.stdin.readline().split())
maps = []
for _ in range(height):
    maps.append(sys.stdin.readline())

# 벽을 부수고 방문했는지, 아닌지에 따라 최단거리가 달라질 수 있으므로 
# visited는 부수지 않고 지나감 / 부수고 지나감 두 가지가 필요하다. 
# 따라서 visited[y][x][벽 파괴여부] 형태로 선언한다.
visited = [[[0] * 2 for _ in range(width)] for _ in range(height)]


def bfs(start, maps, visited, height, width):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = []
    # 최단거리일수록 우선 뽑기 위해 heapq 사용
    heapq.heappush(queue, start)
    while queue:
        cnt, wall, y, x = heapq.heappop(queue)
        visited[y][x][wall] = 1
        # 목적지에 도착했을 경우 cnt를 리턴
        if y == height - 1 and x == width - 1:
            return cnt

        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if 0 <= ny < height and 0 <= nx < width and visited[ny][nx][wall] == 0:
                if maps[ny][nx] == "0" or (maps[ny][nx] == "1" and wall == 0):
                    visited[ny][nx][wall] = 1
                    if maps[ny][nx] == "1":
                        # 벽을 부숴야 하는 경우
                        heapq.heappush(queue, (cnt + 1, wall + 1, ny, nx))
                    else:
                        heapq.heappush(queue, (cnt + 1, wall, ny, nx))
    return -1


# 시작 지점부터 1을 세고 시작해야 하므로 cnt에 1을 넣는다.
print(bfs((1, 0, 0, 0), maps, visited, height, width))
'''