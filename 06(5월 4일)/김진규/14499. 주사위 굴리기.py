# 주사위 자체의 index는 그대로 유지한채 값만 바꾸기
# ex) 상단 => 1, 바닥 => 6, 오른쪽 => 3, 왼쪽 => 4

# 동쪽으로 1칸 굴림
def mv_e():
    dice_lst[1], dice_lst[3], dice_lst[4], dice_lst[6] = dice_lst[4], dice_lst[1], dice_lst[6], dice_lst[3]


# 서쪽으로 1칸 굴림
def mv_w():
    dice_lst[1], dice_lst[3], dice_lst[4], dice_lst[6] = dice_lst[3], dice_lst[6], dice_lst[1], dice_lst[4]


# 북쪽으로 1칸 굴림
def mv_n():
    dice_lst[1], dice_lst[2], dice_lst[5], dice_lst[6] = dice_lst[5], dice_lst[1], dice_lst[6], dice_lst[2]


# 남쪽으로 1칸 굴림
def mv_s():
    dice_lst[1], dice_lst[2], dice_lst[5], dice_lst[6] = dice_lst[2], dice_lst[6], dice_lst[1], dice_lst[5]


# 이동했을 때
# 이동 위치가 0이라면 주사위의 숫자를 그 위치에 입력
# 0이 아니라면 주사위에 그 숫자를 입력하고 그 위치는 0
def mv(x, y):
    if map_arr[x][y] == 0:
        map_arr[x][y] = dice_lst[6]
    else:
        dice_lst[6] = map_arr[x][y]
        map_arr[x][y] = 0


N, M, X, Y, K = map(int, input().split())
# 지도 저장
map_arr = [list(map(int, input().split())) for _ in range(N)]
# 이동 번호 저장
move_list = list(map(int, input().split()))
# 주사위 index의 값을 저장할 리스트
dice_lst = [0] * 7
# 위치를 저장
location = [X, Y]
# 이동 번호를 조회
for move in move_list:
    # 각각의 숫자에 대입하는 방향으로 이동 했을 때
    # 범위가 유효하다면 방향 이동 함수 실행
    # 위치를 이동한 위치로 변경
    # 이동한 위치에서 이동 함수 실행
    # 상단을 출력
    if move == 1 and location[1]+1 < M:
        mv_e()
        location[1] += 1
        mv(location[0], location[1])
        print(dice_lst[1])
    elif move == 2 and location[1]-1 >= 0:
        mv_w()
        location[1] -= 1
        mv(location[0], location[1])
        print(dice_lst[1])
    elif move == 3 and location[0]-1 >= 0:
        mv_n()
        location[0] -= 1
        mv(location[0], location[1])
        print(dice_lst[1])
    elif move == 4 and location[0]+1 < N:
        mv_s()
        location[0] += 1
        mv(location[0], location[1])
        print(dice_lst[1])
