'''
중간에 return을 사용한 게 인상적이었슴!
근데 가장 큰 clean도 종료되면 어떡하지..?
'''




# 상하좌우
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def clean(x, y, d):
    global ans
    # 0이면 청소하고 visited 표식 남기기
    if arr[x][y] == 0:
        arr[x][y] = 2
        ans += 1


    for i in range(4):
        nd = (d+3) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if a[nx][ny] == 0:
            clean(nx, ny, nd)
            return
            # 여기 return은 언제 발동하는가?
            # 네방향 다 검사가 끝났을 때 + 후진 검사를 하지 말라고
            # 언제 살아있는가?
            # 이동할 좌표가 아직 청소전(0)이고 4방향 다 탐색이 끝나면
            ############ 가장 큰 뼈대가 되는 clean도 종료되는 것 아닌가?!?!??!?

        # 방향 유지
        d = nd
    # 뒤로 한칸 이동시 벽(1)이면 종료
    nd = (d+2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    if a[nx][ny] == 1:
        return
    clean(nx, ny, d)



n, m = map(int, input().split())
x, y, d = map(int, input().split())
a = [list(map(int, input().split())) for j in range(n)]

ans = 0
clean(x,y,d)
print(ans)
