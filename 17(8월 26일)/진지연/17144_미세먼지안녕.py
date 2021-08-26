'''
시간초과 뜸
하라고 하는 걸 그대로 구현하면 된다
expand : 원본 arr과 new_arr 둘다 필요함
air_move : 처음에는 네 꼭짓점을 잡고 > 꼭짓점에 도달하면 > 방향을 바꾸는 것을 생각했다.
           그런데 어려워서.. + 인터넷에 더 쉬운 게 있어서 차용했다.
'''


def find_cleaner():
    for r in range(rows):
        if arr[r][0] == -1:
            return [r,0], [r+1,0]

def expand():
    new_arr = [[0]*cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if arr[r][c] <= 0:
                continue

            dust = arr[r][c] // 5
            for d in delta:
                new_r = r + d[0]
                new_c = c + d[1]

                if new_r < 0 or new_r >= rows or new_c < 0 or new_c >= cols:
                    continue
                if arr[new_r][new_c] == -1:
                    continue
                new_arr[new_r][new_c] += dust
                new_arr[r][c] -= dust

    for r in range(rows):
        for c in range(cols):
            arr[r][c] += new_arr[r][c]

def air_move():
    # up
    # 1 - 아래
    temp = arr[up[0]][cols - 1]
    for i in range(cols - 1, 1, - 1):
        arr[up[0]][i] = arr[up[0]][i - 1]
    arr[up[0]][1] = 0

    # 2 - 오른쪽
    temp_1 = arr[0][cols - 1]
    for i in range(up[0] - 1):
        arr[i][cols - 1] = arr[i + 1][cols - 1]
    arr[up[0] - 1][cols - 1] = temp

    # 3 - 위쪽
    temp_2 = arr[0][0]
    for i in range(cols - 2):
        arr[0][i] = arr[0][i + 1]
    arr[0][cols - 2] = temp_1

    # 4 - 왼쪽
    for i in range(up[0] - 1, 1, -1):
        arr[i][0] = arr[i - 1][0]
    arr[1][0] = temp_2

    # down
    # 1- 위쪽
    temp = arr[down[0]][cols - 1]
    for i in range(cols - 1, 1, -1):
        arr[down[0]][i] = arr[down[0]][i - 1]
    arr[down[0]][1] = 0

    # 2 오른쪽
    temp_1 = arr[rows- 1][cols - 1]
    for i in range(rows - 1, down[0] + 1, -1):
        arr[i][cols - 1] = arr[i - 1][cols - 1]
    arr[down[0] + 1][cols - 1] = temp

    # 3 - 아래쪽
    temp_2 = arr[rows- 1][0]
    for i in range(cols - 2):
        arr[rows- 1][i] = arr[rows- 1][i + 1]
    arr[rows- 1][cols - 2] = temp_1

    # 4 - 왼쪽
    for i in range(down[0] + 1, rows - 1):
        arr[i][0] = arr[i + 1][0]
    arr[rows- 2][0] = temp_2
    
rows,cols,time = map(int, input().split())
delta = [[-1,0], [0,-1], [1,0], [0,1]]
arr = [list(map(int, input().split())) for _ in range(rows)]
up, down = find_cleaner()

for i in range(time):
    expand()  # 미세먼지 이동
    air_move()  # 공기청정기 작동

total = 0
for i in range(rows):
    for j in range(cols):
        if arr[i][j] > 0:
            total += arr[i][j]
print(total)
