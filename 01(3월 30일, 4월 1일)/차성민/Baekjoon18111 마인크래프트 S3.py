#백준 18111 마인크래프트 S3
#완전탐색, 실패, 완전탐색 복습 요망

# N X M 리스트
# 블록제거 - 2초, 블록 추가 - 1초
# 땅 고르지 작업 최소 시간, 땅의 높이 출력(땅 높이 최대 256)
# 답이 여러개있다면 땅의 높이가 가장 높은 것을 출력. (조건)  오름차순으로 진행하여 해결
import sys
sys.stdin = open('18111.txt', 'r')

N, M, B = map(int, input().split()) # 리스트, 인벤토리 안 블록
area = [list(map(int, input().split())) for _ in range(N)]

res = 2976000000 #결과 시간을 넣을 변수
h = 0  #결과 높이를 넣을 변수

# 모든 높이일 때의 카운트 값들을 비교해야함(0~ 256)
#기준 높이로 맞출 때 더해줘야하는 plus값을 기존 B에 합한 값이 낮출 때 필요한 minus값보다 작아야 함.
# 오름차순으로 k가 증가하므로 시간이 같을 때에는 높이가 높은것이 나옴 반대라면 내림차순으로.
for k in range(257):
    # 리스트 값이 기준높이 k보다 작으면 minus에 크면 plus에 추가해줌. [time = 2 * plus + minus]
    plus = 0
    minus = 0
    for i in range(N):
        for j in range(M):
            if area[i][j] < k:
                minus += (k - area[i][j])
            else:
                plus += (area[i][j] - k)

    inv = plus + B  # 인벤토리 안에 plus 개수 만큼을 더해줌
    #위에서 기존 B + plus값이 minus 보다 작으면 조건이 성립안됨 -> continue.
    if inv < minus:
        continue

    time = 2 * plus + minus

    if res >= time:
        res = time
        h = k
print(res, h)


