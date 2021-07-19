#백준2631 줄세우기

'''
실패

가장큰 수  -> 뒤로, 가장 작은 수 -> 앞으로
여기까지는 생각 함.

다른 사람들 풀이 파악 진행.

LIS(최장 증가 부분 수열)문제라 함.

풀이는 시간을 고려하여 LIS로 사용하거나   O(nlogn)
이중 for문을 도는 형태의 dp풀이가 존재한다. O(n^2)

'''


#풀이 1  (LIS)   O(nlogn)
# 이미 오름차순으로 정렬되어 있는 것들은 이동시키지 않아야 함.

import sys

input = sys.stdin.readline

N = int(input())
children = [int(input()) for _ in range(N)]
LIS = [0]
length = 0

for num in children:
    if num > LIS[-1]:
        LIS.append(num)
        length += 1
    else:
        left = 0
        right = len(LIS)

        while left < right:
            mid = (left + right) // 2

            if LIS[mid] >= num:
                right = mid
            else:
                left = mid + 1

        LIS[right] = num

print(N - length)

'''
풀이 2 dp O(n^2)

N = int(input())  # 아이들의 수
people = [int(input()) for _ in range(N)]  # 아이들 번호 순서 정보

# 2차원 dp
dp = [[0] * N for _ in range(N)]
# 가장 긴 증가하는 부분수열
for i in range(N):
    dp[i][i] = 1  # i를 시작점으로 설정.
    for j in range(i + 1, N):
        for k in range(j):
            if people[k] < people[j]:
                dp[i][j] = max(dp[i][j], dp[i][k] + 1)

# 가장 긴 증가하는 수열 길이 계산
lis = 0
for i in range(N):
    lis = max(lis, max(dp[i]))

# 전체 길이 - 가장 긴 증가하는 부분수열
answer = N - lis
print(answer)
    
'''
