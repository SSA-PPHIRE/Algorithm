#백준 1806 부분합 G4
#투 포인터 문제
#1644 소수의 연속합과 비슷하게 접근.

import sys
sys.stdin = open('text/1806.txt', 'r')

n, s = map(int, input().split()) # 수열의 길이, 최소 부분합

arr = list(map(int, input().split()))

res = 0 # 답 출력용
l, r = 0, 1 #포인터 설정
temp = arr[0]
cnt = 1

while True: # 끝까지 돌리자
    if temp >= s: #현재까지의 합이 s보다 크거나같은 조건 만족하면
        if cnt < res: # 이미 이전에 만족하는 개수가 res에 있는상황이고, cnt가 더 적은 개수라면 덮어 씌워줌.
            res = cnt
        if res == 0:  #처음으로 만족하는 개수가 나오면 res는 cnt
            res = cnt
        cnt -= 1
        temp -= arr[l]
        l += 1
    elif r == len(arr): #끝까지 오면 break
        break
    else: #현재까지의 합이 s보다 작으면 우측값 추가 하고 개수도 추가하고 우측 포인터 증시키고 진행함.
        temp += arr[r]
        cnt += 1
        r += 1

print(res)