'''
주사위의 면들  : 도는 방향에 따라 switch
주사위의 맨 위& 맨 아래 : 칸에 따라 change

0 : 아래
1: 동
2: 남
3: 서
4: 북
5 : 위
'''

def walls(dir):
    global dice
    if dir == 1:
        dice[0], dice[5], dice[1], dice[2], dice[3], dice[4] = dice[1], dice[3], dice[5], dice[2], dice[0], dice[4]
    elif dir == 2:
        dice[0], dice[5], dice[1], dice[2], dice[3], dice[4] = dice[3], dice[1], dice[0], dice[2], dice[5], dice[4]
    elif dir == 3:
        dice[0], dice[5], dice[1], dice[2], dice[3], dice[4] = dice[2], dice[4], dice[1], dice[5], dice[3], dice[0]
    else:
        dice[0], dice[5], dice[1], dice[2], dice[3], dice[4] = dice[4], dice[2], dice[1], dice[0], dice[3], dice[5]


def position(r,c,dir):
    global stack, arr
    new_r = r + delta[dir][0]
    new_c = c + delta[dir][1]

    if 0 <= new_r < rows and 0 <= new_c < cols:
        # 회전시키기
        walls(dir)

        # 칸에 따라 바꾸기
        if arr[new_r][new_c] == 0:
            arr[new_r][new_c] = dice[0]
        else:
            dice[0] = arr[new_r][new_c]
            arr[new_r][new_c] = 0
        print(dice[5])
        stack.append([new_r, new_c])

    else:       # 칸을 벗어나면 해당 명령을 무시한다.
        stack.append([r,c])


rows, cols, root_r, root_c, total = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(rows)]
dirs = list(map(int, input().split()))
dice = [0]*6
delta = [[0,0], [0,1], [0,-1], [-1,0], [1,0]]


stack = [[root_r, root_c]]
for i in range(total):

    r, c = stack.pop(0)
    position(r,c,dirs[i])







