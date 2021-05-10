# 첫번째 시도
# 시간초과
def check(idx, w, v):
    global max_val
    if idx == N:
        if max_val < v:
            max_val = v
        return

    if w+things[idx][0] <= K:
        check(idx+1, w+things[idx][0], v+things[idx][1])
    check(idx+1, w, v)


N, K = map(int, input().split())
things = [tuple(map(int, input().split())) for _ in range(N)]
max_val = 0
check(0, 0, 0)
print(max_val)
######################################################
# 두번째 시도
# 더 느리다...
for i in range(1<<N):
    sum_val = 0
    sum_weight = 0
    for j in range(N):
        if i & (1<<j):
            sum_weight += things[j][0]
            sum_val += things[j][1]
            if sum_weight > K:
                break
    else:
        if sum_val > max_val:
            max_val = sum_val
print(max_val)

####################################################
# 세번째 시도
# 알고리즘을 찾아본 후 다시 풀어봄
N, K = map(int, input().split())
# things의 index를 DP와 맞추기 위해 하나를 추가
no_item = [(0, 0)]
# 입력받은 값들
things = [tuple(map(int, input().split())) for _ in range(N)]
# 처음에 (0, 0)을 더해줌
things = no_item + things
# DP는 물건의 수+1의 행과 무게+1의 열의 수 만큼 선언
DP = [[0]*(K+1) for _ in range(N+1)]

# 0번째 물건은 0,0 이므로 반복할 필요가 없다.
# j는 단순히 현재 담을려는 무게를 의미
for i in range(1, N+1):
    for j in range(K+1):
        # 만약 물건의 무게가 현재 담으려는 무게보다 무겁다면 이전 물건의 DP값(가치)을 대입
        if things[i][0] > j:
            DP[i][j] = DP[i-1][j]
        # 만약 물건의 무게가 혀재 담으려는 무게보다 가볍다면
        # 이전 물건의 현재 무게일 때의 DP값(가치)과
        # 현재 담으려는 물건의 가치 + 이전까지 구했던 가치들중 현재 물건의 무게를 뺀 가치를 비교
        else:
            DP[i][j] = max(DP[i-1][j], things[i][1] + DP[i-1][j - things[i][0]])
print(DP[-1][-1])
