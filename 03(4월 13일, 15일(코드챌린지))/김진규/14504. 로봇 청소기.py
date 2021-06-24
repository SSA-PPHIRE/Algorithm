
###################################
# 문제 말이 너무 어려움!
# dfs는 갔던 방향 그대로 다시 나오지만
# 이 문제는 마지막으로 확인한 방향에서 반대로 나왔을 경우
# 그곳이 벽이면 종료 아니면 계속 반복
# 이 것만 이해한다면 상대적으로 쉽게 구현할 수 있을 
####################################
def check(x, y, direct):
    global cnt, flag
    # 청소가 끝났을 때 종료
    if flag == 0:
        return
    # 만약 청소하지 않은 공간이라면 청소한 것을 표시후 cnt 증가
    if map_arr[x][y] == 0:
        cnt += 1
        map_arr[x][y] = 2

    for i in range(4):
        # 왼쪽 방향으로 진행하기 때문에 -1
        direct -= 1
        # 0보다 작아지면 4를 더해서 index 유지
        if direct < 0:
            direct += 4
        xx = x + dx[direct]
        yy = y + dy[direct]
        # 만약 이동한 위치가 청소하지 않았다면 청소 실행
        if map_arr[xx][yy] == 0:
            check(xx, yy, direct)
    # 네 방향을 모두 확인했을 때 모두 청소 했거나 벽이 있다면
    else:
        # 바라보고 있는 방향 그대로 뒤로 돌아감
        x -= dx[direct]
        y -= dy[direct]
        # 만약 돌아간 위치가 벽이 아니라면
        if map_arr[x][y] != 1:
            # 계속해서 진행
            check(x, y, direct)
        # 벽이라면 청소종료를 알리고 return
        else:
            flag = 0
            return


N, M = map(int, input().split())
r, c, d = map(int, input().split())
map_arr = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt, flag = 0, 1
# 만약 r,c 가 벽이면 0을 출력
if map_arr[r][c] == 1:
    print(cnt)
# 그렇지 않다면 함수를 실행 후 출력
else:
    check(r, c, d)
    print(cnt)

# 재귀 함수
###########################################################################
# 단순 이동
# 굳이 다시 돌아갈 필요가 없다는 것을 알아서 dfs를 사용하지 않음

def check(r, c ,d):
    global cnt
    # 현재 위치 청소
    map_arr[r][c] = 2
    # cnt 증가
    cnt += 1
    # 입력받은 변수를 다시 옮김 < 굳이 필요 없을듯
    x, y, direct = r, c, d
    while True:
        for i in range(4):
            direct -= 1
            if direct < 0:
                direct += 4
            xx = x + dx[direct]
            yy = y + dy[direct]
            # 만약 다음 좌표가 청소를 하지 않았다면
            # 청소하고 cnt 증가후 그곳으로 이동 후 다시 처음부터 진행
            if map_arr[xx][yy] == 0:
                map_arr[xx][yy] = 2
                cnt += 1
                x = xx
                y = yy
                break
        # 네방향 확인 후 모두 청소 or 벽이라면
        else:
            # 바라보는 방향 그대로 후진
            x -= dx[direct]
            y -= dy[direct]
            # 벽이 아니라면 그대로 계속
            if map_arr[x][y] != 1:
                continue
            # 벽이라면 그만
            else:
                break


N, M = map(int, input().split())
r, c, d = map(int, input().split())
map_arr = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
if map_arr[r][c] == 1:
    print(cnt)
else:
    check(r, c, d)
    print(cnt)
