#백준 12865 평범한 배낭 G5

import sys
sys.stdin = open('text/12865.txt', 'r')

'''
쪼갤 수 있는가? -> 무게 대비 가치 높은 물건들부터 담으면 끝 (그리디)
쪼갤 수 없다 -> DP  (재귀 or 재귀 없이)

https://velog.io/@huttzza/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-0-1-Knapsack-Problem
https://gsmesie692.tistory.com/113

접근법 
1. 무게나 물품 수를 기준으로 오름차순과 내림차순 기준으로 매칭시켜볼까함 (불가)
2. 분할 가능한 배낭 문제? 아니네 -> 0-1 knapsack문제 => DP

case)
 1 - 배낭에 들어가지만 넣음
 2 - 배낭에 들어가지만 안 넣음
 3 - 배낭에 안 들어감

w는 총 무게 합   0< w <= W
DP[i][w]는 i번째까지 item고려하고, 무게 한도가 w일때의 최적 결과

위의 케이스에서

1,2번 케이스 : wi <= w
  - 1번 : DP[i-1][w-wi] + pi
  - 2번 : DP[i-1][w]

3번 케이스: wi > w
  - 3번 : DP[i-1][w]

1,2   / 3 케이스 중 최대 이득값이 답.

'''

n, k = map(int, input().split()) #물품의 수, 버틸 수 있는 무게

arr = []  #DP를 위해 2중 리스트 생성
for _ in range(n+1):
    arr.append([0] * (k+1))

for i in range(1, n + 1):
    item, value = map(int, input().split())
    for j in range(1, k + 1):
        if item <= j:   #  1,2번 케이스
            arr[i][j] = max(arr[i - 1][j], arr[i - 1][j - item] + value)
        else: # 3번 케이스라면(안들어간다면) 덮어씌워주고 진행.
            arr[i][j] = arr[i - 1][j]

print(arr[n][k])
