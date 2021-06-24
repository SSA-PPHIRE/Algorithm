K, N = map(int, input().split())
lan_lst = [int(input()) for _ in range(K)]

# 최소값
min_val = 1
# 최대값
max_val = max(lan_lst)
# 반복문
while True:
    # 최대 값이 최소 값 보다 작다면 break
    if max_val < min_val:
        break
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
        min_val = mid_val + 1
    # 갯수들의 합이 N보다 작다면
    elif sum_val < N:
        # 최댓값은 중간값으로
        max_val = mid_val - 1

print(max_val)

'''
이분탐색은 중간 값을 포함하지 않고 다시 탐색한다는 사실을 다시 한 번 되새기는 기회가 되었다.
재귀 함수에서 return 값 설정에 대해 다시 한 번 보는 기회가 되었다.
극단적인 경우도 고려해야 한다!
'''
