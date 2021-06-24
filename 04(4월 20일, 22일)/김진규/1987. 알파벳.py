# 딕셔너리로 저장 => 실패
# cnt를 set에 저장 후 최댓값 => 실패
# 배열로 저장해서 in 사용 => 실패
# 숫자로 바꿔서 시도 => 성공

def check(x, y, c, cnt):
    # 부가 옵션
    ##########################
    global max_val, flag
    if flag == 1:
        return
    if cnt == (N * M):
        max_val = cnt
        flag = 1
        return
    #############################
    if cnt > max_val:  # 매번 cnt와 최댓값을 비교
        max_val = cnt
    # 알파벳 방문 체크
    ord_lst[c] = 1
    # 현재 위치 방문 체크
    visited[x][y] = 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < N and 0 <= yy < M and visited[xx][yy] == 0 and not ord_lst[map_arr[xx][yy]]:
            check(xx, yy, map_arr[xx][yy], cnt+1)
            visited[xx][yy] = 0
            ord_lst[map_arr[xx][yy]] = 0


N, M = map(int, input().split())
# 알파벳을 숫자로 바꿈
map_arr = [list(map(lambda x: ord(x)-65, input())) for _ in range(N)]
# 방문체크
visited = [[0] * M for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
max_val = 0
flag = 0
# 알파벳을 정수로 바꾼 것을 저장할 리스트
ord_lst = [0]*26
check(0, 0, map_arr[0][0], 1)
print(max_val)
