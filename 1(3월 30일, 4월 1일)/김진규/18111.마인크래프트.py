# 단순히 최대값과 최솟값을 목표로 잡고 계산하려고 하였다.
# 실패하였다...ㅜ

N, M, B = map(int, input().split())
b_arr = []
# 배열의 최대값
max_val = 0
# 배열의 최솟값
min_val = 300
# 배열의 합
sum_val = 0
# 배열의 차를 계산할 배열
cal_arr = [[0]*M for _ in range(N)]
# 입력되는 배열을 넣고 배열의 합과 최대, 최솟값을 구한다.
for _ in range(N):
    tmp = list(map(int, input().split()))
    sum_val += sum(tmp)
    b_arr.append(tmp)
    max_val = max(max_val, max(tmp))
    min_val = min(min_val, min(tmp))

# 배열의 합의 평균을 반올림해서 구했다.
avg_val = round(sum_val / (N*M))
# 배열의 차들의 합
sum_cal = 0
# 최솟값까지 뺀다고 가정했을 때 최댓값으로 부터 빼야할 갯수
sum_max = 0
# 최댓값까지 더한다고 가정했을 때 최솟값으로 부터 더해야할 갯수
sum_min = 0
# 각 배열의 항목에서 평균을 뺀다.
for i in range(N):
    for j in range(M):
        cal_arr[i][j] = b_arr[i][j] - avg_val
        sum_cal += cal_arr[i][j]
        sum_min += b_arr[i][j] - min_val
        sum_max += max_val - b_arr[i][j]

# 단순하게 생각했다
# 초의 비율이 1:2 이므로 평균값의 차이의 비율이 1보다 작다면 더하고
# 1보다 크다면 뺐다.
if sum_cal + B >= 0 and ((max_val - min_val) * (1/3) + min_val) < avg_val:
    # 최댓값까지 넣기
    res = sum_min
    ans = max_val
else:
    # 최솟값 빼기
    res = sum_max * 2
    ans = min_val

print(res, ans)