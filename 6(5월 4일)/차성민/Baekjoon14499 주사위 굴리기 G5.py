#백준 14499 주사위 굴리기 G5 삼성역테 기출
# 시뮬레이션 문제

# (y, x) (열, 행)
# 핵심 : 동 서 남 북 으로 이동할 때 주사위 면의 변화파악하고 이걸 식으로 만드는 것

import sys
sys.stdin = open('text/14499.txt', 'r')

n, m, x, y, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
order = list(map(int, input().split()))  #명령어들 리스트에 넣어줌
'''  주사위 모양
0 2 0
4 1 3
0 5 0
0 6 0
'''
dice = [[0,0,0], [0,0,0], [0,0,0], [0,0,0]]
dx = [0, 0, 0, -1, 1]  # 1,2,3,4로 order가 오므로 0번째는 0을 넣어줌
dy = [0, 1, -1, 0, 0]  # 동, 서, 북, 남


def chk(order, arr, dice, c, r):
    x = c + dx[order]
    y = r + dy[order]
    if 0 <= x < n and 0 <= y < m:
        if order == 1:  # 동(order == 1)

            dice[1][1], dice[1][2], dice[3][1], dice[1][0] = dice[1][0], dice[1][1], dice[1][2], dice[3][1]
            print(dice[1][1])

        elif order == 2:  # 서(order == 2)
            dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[1][1], dice[1][2], dice[3][1], dice[1][0]
            print(dice[1][1])

        elif order == 3:  # 북(order == 3)

            dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[1][1], dice[2][1], dice[3][1], dice[0][1]
            print(dice[1][1])

        elif order == 4:  # 남(order == 4)
            dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[3][1], dice[0][1], dice[1][1], dice[2][1]
            print(dice[1][1])

        if arr[x][y] == 0: #0 만나면 아래면 값 넣어줌.
            arr[x][y] = dice[3][1]

        else:  #0 아니면 바닥면에 자리 값 넣어줌.
            dice[3][1] = arr[x][y]
            arr[x][y] = 0

        return x, y

    else: #범위 밖이면 리턴하고 다음번으로 넘어감
        return c, r


for i in range(k):
    x, y = chk(order[i], arr, dice, x, y) #명령어 순서, 배열, 주사위, 좌표값 활용해서 체크
