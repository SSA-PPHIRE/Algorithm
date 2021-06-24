########################
# 원리를 간단하게 말하자면
# dfs로 ㅏ 모양을 제외한 나머지를 찾고
# ㅏ 모양만 따로 찾아서 비교
#########################
# 길이가 4인 블록들을 모두 계산하는 함수
def check(x, y, tmp_sum, cnt):
    global max_sum
    # 시작시 방문체크
    visited[x][y] = 1
    # 길이가 4라면 최대값과 비교 후 return
    if cnt == 4:
        max_sum = max(tmp_sum, max_sum)
        return
    # 4방향 탐색후 재귀
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < N and 0 <= yy < M and visited[xx][yy] == 0:
            check(xx, yy, tmp_sum+map_arr[x][y], cnt+1)
            # 돌아올 때 방문 체크 해제
            visited[xx][yy] = 0
    # 끝내기 전 방문체크 해제
    visited[x][y] = 0


# ㅏ모양을 처리하는 함수
def check2(x, y):
    global max_sum
    # 가운데는 항상 포함하고
    # 나머지는 십자 모양에서 하나씩 뺀다고 생각
    center = map_arr[x][y]
    # 십자모양에서 뺄 방향을 설정
    for i in range(4):
        tmp = center
        # 나머지 값을 더해서 구함
        for j in range(3):
            k = (i+j) % 4
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx < N and 0 <= yy < M:
                tmp += map_arr[xx][yy]
            # 만약 3방향 모두 포함되지 않는다면 break
            else:
                break
        # 최대값 비교
        if tmp > max_sum:
            max_sum = tmp


N, M = map(int, input().split())
map_arr = [list(map(int, input().split())) for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
max_sum = 0
visited = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        check(i, j, 0, 0)
        check2(i, j)

print(max_sum)
