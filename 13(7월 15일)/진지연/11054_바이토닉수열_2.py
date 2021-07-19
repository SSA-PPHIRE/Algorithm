'''
2. 줄세우기 (G5) [숙]
https://www.acmicpc.net/problem/2631
얘를 풀고 나서 이해했다..

LIS를 찾는다

arr[i]가 꼭짓점인 LIS를 찾는다
앞에서 + 뒤에서
합쳐서 제일 큰 것 -1 : 가장 긴 바이토닉 수열
'''

n = int(input())
arr = list(map(int, input().split()))


def find_lis():
    dp = [1 for _ in range(n)]

    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return dp

dp_forward = find_lis()
arr = arr[::-1]
dp_backward = find_lis()


dp = []
for a, b in zip(dp_forward, dp_backward[::-1]):
    dp.append(a+b)

print(max(dp)-1)
