# 무식하게 다 저장해놓고 했다...
# 승철님 코드를 보니 필요한 만큼만 계산하였다!

# 최대 400만
num_lst = [0, 1]*2000001
# 1을 0으로
num_lst[1] = 0
# 2를 소수에 추가
prime = [2]
# 3부터 홀수를 (400만)^(1/2)만큼 탐색후 소수면 나머지를 모두 0으로
for i in range(3, 2001, 2):
    if num_lst[i] == 1:
        prime.append(i)
        n = 1
        while True:
            num_lst[i*n] = 0
            n += 1
            if i*n >= 4000001:
                break
# 남은 소수들을 추가
for i in range(2001, 4000001):
    if num_lst[i] == 1:
        prime.append(i)

N = int(input())
cnt = 0
# i => 더하기 시작하는 위치
for i in range(len(prime)):
    sum_val = 0
    if prime[i] == N:
        cnt += 1
        break
    if prime[i] > N:
        break
    # j => 더하는 위치
    for j in range(i, len(prime)):
        sum_val += prime[j]
        if sum_val == N:
            cnt += 1
            break
        elif sum_val > N:
            break
print(cnt)

############## 좀 더 최적화 ##################
# 시간이 고만고만...


import math

N = int(input())
num_lst = [0 if i < 3 else 1 for i in range(N+1)]
prime = [2]
root_N = math.floor(math.sqrt(N))
for i in range(N+1):
    if i % 2 == 0:
        num_lst[i] = 0

for i in range(3, root_N+1, 2):
    if num_lst[i] == 1:
        prime.append(i)
        n = 1
        while True:
            num_lst[i*n] = 0
            n += 1
            if i*n > N:
                break
# 남은 소수들을 추가
for i in range(root_N+1, N+1):
    if num_lst[i] == 1:
        prime.append(i)

cnt = 0
# i => 더하기 시작하는 위치
for i in range(len(prime)):
    sum_val = 0
    if prime[i] == N:
        cnt += 1
        break
    if prime[i] > N:
        break
    # j => 더하는 위치
    for j in range(i, len(prime)):
        sum_val += prime[j]
        if sum_val == N:
            cnt += 1
            break
        elif sum_val > N:
            break
print(cnt)
