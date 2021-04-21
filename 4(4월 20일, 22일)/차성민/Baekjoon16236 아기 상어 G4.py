#백준 16236 아기 상어 G4
#BFS 문제, 시뮬레이션 문제, 실패
# 조건들 다루기가 너무 까다로움.
# 참고 : https://gingerkang.tistory.com/70

from collections import deque
import sys
sys.stdin = open('text/16236.txt', 'r')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def BFS(c, r):
    global shark, res

    pos = shark[1]
    q = deque()
    q.append(pos)
    dist = 0
    visited = [[0] * n for _ in range(n)] #방문 체크위해 visited 활용
    visited[pos[1]][pos[0]] = 1
    fish = [] #먹을 수 있는 물고기들 넣기 위한 리스트 생성
    flag = 0

    while q:
        dist += 1

        for _ in range(len(q)):
            xx, yy = q.popleft()

            for i in range(4): #사방향 탐색
                x = xx + dx[i]
                y = yy + dy[i]

                if 0 <= x < n and 0 <= y < n: #범위를 벗어나지 않았으면 진행
                    if arr[y][x] <= shark[0] and visited[y][x] == 0: #아기상어보다 크지 않은 값과 오지 않은곳이라면
                        visited[y][x] = 1
                        # 먹을 수 있는거면
                        if 0 < arr[y][x] < shark[0]:
                            fish.append((x,y))
                            flag = 1
                        else:
                            q.append((x,y))
        if fish: #fish리스트에 먹을 수 있는 물고기의 좌표가 들어있다면 break로 나와서 물고기 부분 부터 처리해 줘야 함.
            break

    # 물고기가 여러마리라면 가장 왼쪽에 있는 물고기 -> sort 함수 활용
    if fish:
        fish = sorted(fish, key = lambda x:(x[1], x[0])) # 값을 역으로 해서 정렬해주어야 함(람다 활용 필요)  거리, x좌표, y좌표 순으로 정렬
        arr[fish[0][1]][fish[0][0]] = 9
        arr[pos[1]][pos[0]] = 0
        shark[1] = fish[0]
        shark[2] -= 1
        if shark[2] == 0:
            shark[0] += 1
            shark[2] = shark[0]
        res += dist
        return True
    else:
        return False

# 기본 세팅
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# 현재 상어의 크기, 좌표, 먹은 물고기 수.. 너무 생각할게 많음 -> 묶자
# dist = 0
# fish = 0
# size = 2
shark = [2, (0,0), 2] # 크기, 좌표, 먹은 물고기의 수를 하나의 리스트로 통합
res = 0

# 아기 상어 위치, 크기, 레벨? 활용
for r in range(n):
    for c in range(n):
        if arr[r][c] == 9:
            shark[1] = (c, r) # 위치 저장
            arr[r][c] = 0 # 값을 바꾸지 않으면 나중에 자기 자신 먹는 케이스 나올 수 있음.
            break

while True:
    if not BFS(r, c): # BFS에서 어떤 값들을 인자로 전달해 줄 것인가? 좌표와 크기를 함께? 일단 좌표만 주자
        break
print(res)



'''
3
9 2 2
2 2 3
1 3 1
'''
