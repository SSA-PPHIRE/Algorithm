########################
# 시간초과!
#######################
# 원리를 간단하게 말하자면
# bfs로 ㅏ 모양을 제외한 나머지를 찾고
# ㅏ 모양만 따로 찾아서 비교
#########################
def check(x, y):
    global cnt, tmp_sum, max_sum
    cnt += 1
    visited[x][y] = 1
    tmp_sum += map_arr[x][y]

    if cnt == 4:
        max_sum = max(tmp_sum, max_sum)
        return

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < N and 0 <= yy < M and visited[xx][yy] == 0:
            check(xx, yy)
            cnt -= 1
            visited[xx][yy] = 0
            tmp_sum -= map_arr[xx][yy]


def check2(x, y):
    global max_sum
    tmp = 0
    tmp_cnt = 0
    tmp += map_arr[x][y]
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < N and 0 <= yy < M:
            tmp += map_arr[xx][yy]
            tmp_cnt += 1
    if tmp_cnt == 3:
        max_sum = max(max_sum, tmp)
    elif tmp_cnt == 4:
        for i in range(4):
            tmp_sum = tmp
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < N and 0 <= yy < M:
                tmp_sum -= map_arr[xx][yy]
                max_sum = max(max_sum, tmp_sum)

N, M = map(int, input().split())
map_arr = [list(map(int, input().split())) for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
max_sum = 0

for i in range(N):
    for j in range(M):
        visited = [[0]*M for _ in range(N)]
        cnt = 0
        tmp_sum = 0
        check(i, j)
        check2(i, j)

print(max_sum)
