# 크기가 같으면 지나갈 순 있다 먹을순 없음
# 크기가 크면 못 지나감
# 작으면 먹는다
# 한칸엔 물고기 최대 1마리
# 1초에 상하좌우 한칸씩 이동

# 더이상 먹을 수 있는게 없다면 엄마상어
# 가까운 거리부터 먹는다.
# 거리는 최솟값
# 위에서 아래로 , 왼쪽에서 오른쪽 순으로

# 이동은 1초
# 아기상어는 9, 처음 크기는 2
# 아기상어 크기만큼 먹으면 크기 1 증가후 먹은 갯수는 초기화
# debug용 pprint
import pprint

# 이젠 필수가 되어버린 deque
from collections import deque


def bfs(r, c):
    # 먹은 수와 상어의 크기를 전역 변수로 설정
    global ate, size
    # q에 현재의 좌표와 저장할 거리를 추가
    q = [(r, c, 1)]
    # 방문 체크
    visited[r][c] = 0
    # q를 deque로 만들어 준다
    q = deque(q)
    # 먹을 수 있는 좌표들
    can_ate = []
    while q:
        # 기존의 bfs처럼 앞에서 부터 뽑아낸다.
        x, y, cnt = q.popleft()
        # delta 탐색
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            # 범위 내에 xx와 yy가 존재하고 방문체크 되지 않았으며 물고기의 크기가 같거나 작을 때
            if 0 <= xx < N and 0 <= yy < N and visited[xx][yy] == -1 and map_arr[xx][yy] <= size:
                # 물고기의 크기가 작다면 can_ate에 추가
                if 0 < map_arr[xx][yy] < size:
                    can_ate.append((xx, yy, cnt))
                # 방문체크
                visited[xx][yy] = cnt
                # q에 추가
                q.append((xx, yy, cnt+1))
    # 만약 can_ate가 없다면 -1을 반환
    if can_ate == []:
        return -1
    # 만약 존재한다면
    else:
        # 먹은 수 1 증가
        ate += 1
        # 만약 사이즈 만큼 먹었다면 사이즈 증가 후 먹은 수 초기화
        if ate == size:
            size += 1
            ate = 0
        # 거리가 가장 작고 (x[2])
        # 가장 위에 있는 것부터 탐색하며 (x[0])
        # 다음으로 가장 왼쪽에 있는 것부터 먹는다. (x[1])
        can_ate.sort(key=lambda x: (x[2],x[0],x[1]))
        # 정렬한 배열의 가장 첫번째를 반환
        return can_ate[0]


# 공간의 크기
N = int(input())
# 공간 상태
map_arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if map_arr[i][j] == 9:
            # 상어를 찾고 0으로 초기화
            # 초기화 하지 않는다면 숫자가 높으므로 지나가지 못한다.
            map_arr[i][j] = 0
            # 상어의 위치 저장
            shark = (i, j)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
####### 기본 설정
ate = 0  # 먹은 수
size = 2  # 상어 크기
total = 0  # 총거리
#######
while True:
    # 방문 체크를 반복할 때마다 초기화
    visited = [[-1] * N for _ in range(N)]
    # 반환된 좌표를 다시 상어의 위치로 저장
    shark = bfs(shark[0], shark[1])
    # 만약 좌표가 아닌 -1이라면 break
    if shark == -1:
        break
    # 좌표라면 물고기를 먹었으므로 0으로 변환
    map_arr[shark[0]][shark[1]] = 0
    # 총거리에 이동 거리를 더함
    total += shark[2]

print(total)
