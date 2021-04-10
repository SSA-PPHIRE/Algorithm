##################################
# 곧 주석 추가 예정 안까먹는다면?!
###################################
# 문제 말이 너무 어려움!
# dfs는 갔던 방향 그대로 다시 나오지만
# 이 문제는 마지막으로 확인한 방향에서 반대로 나왔을 경우
# 그곳이 벽이면 종료 아니면 계속 반복
# 이 것만 이해한다면 상대적으로 쉽게 구현할 수 있을 
####################################

def check(x, y, direct):
    global cnt, flag
    if flag == 0:
        return
    if map_arr[x][y] == 0:
        cnt += 1
        map_arr[x][y] = 2

    for i in range(4):
        direct -= 1
        if direct < 0:
            direct += 4
        xx = x + dx[direct]
        yy = y + dy[direct]
        if map_arr[xx][yy] == 0:
            check(xx, yy, direct)
    else:
        x -= dx[direct]
        y -= dy[direct]
        if map_arr[x][y] != 1:
            check(x, y, direct)
        else:
            flag = 0
            return


N, M = map(int, input().split())
r, c, d = map(int, input().split())
map_arr = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt, flag = 0, 1
if map_arr[r][c] == 1:
    print(cnt)
else:
    check(r, c, d)
    print(cnt)

# 재귀 함수
###########################################################################
# 단순 이동

def check(r, c ,d):
    global cnt
    map_arr[r][c] = 2
    cnt += 1
    x, y, direct = r, c, d
    while True:
        for i in range(4):
            direct -= 1
            if direct < 0:
                direct += 4
            xx = x + dx[direct]
            yy = y + dy[direct]
            if map_arr[xx][yy] == 0:
                map_arr[xx][yy] = 2
                cnt += 1
                x = xx
                y = yy
                break
        else:
            x -= dx[direct]
            y -= dy[direct]
            if map_arr[x][y] != 1:
                continue
            else:
                break


N, M = map(int, input().split())
r, c, d = map(int, input().split())
map_arr = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt, flag = 0, 1
if map_arr[r][c] == 1:
    print(cnt)
else:
    check(r, c, d)
    print(cnt)
