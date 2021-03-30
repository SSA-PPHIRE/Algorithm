K, N = map(int, input().split())
lan_lst = [int(input()) for _ in range(K)]

# 최소값
min_val = 0
# 최대값
max_val = max(lan_lst)
# 반복문
while True:
    # 중간 값
    mid_val = (min_val + max_val)//2
    # 합
    sum_val = 0
    # 갯수들의 합
    for num in lan_lst:
        sum_val += num//mid_val
    # 갯수들의 합이 N보다 크거나 같을 때
    if sum_val >= N:
        # 최솟값은 중간값으로
        min_val = mid_val
        # 만약 최대값이 최솟값+1 보다 작다면 종료
        if max_val <= min_val + 1:
            break
    # 갯수들의 합이 N보다 작다면
    elif sum_val < N:
        # 최댓값은 중간값으로
        max_val = mid_val

print(min_val)