#백준 1654 랜선 자르기 S3
# 이분 탐색 활용 문제

import sys
sys.stdin = open('1654.txt', 'r')

K, N = map(int, input().split())
arr = list(int(input()) for _ in range(K))

# Point: end를 막대들 중 최고치의 길이로 할 것!
l, r = 1, max(arr)  #left, right
while (l<= r):
    sum = 0
    c = (l + r) // 2   #중앙 지점 설정
    for num in arr:
        sum += (num // c)
    if sum >= N: # 랜선수가 N보다 같거나 많다면
        ans = c #정답 ans를 여기에서 지정해주지 않으면 원하는
        l = c + 1 # l 아래 수들은 보나마나이므로 l을 c+1로 설정해주고 진행
    else:  #랜선수가 N보다 작다면
        r = c - 1 #조건을 만족 못 하니까 r을 c-1로 진행
print(ans)






# 시간 초과
# length = 1
# sum = 0
# while True:
#     for i in arr:
#         a = int(i / length)
#         sum += a
#     if sum > N:
#         length += 1
#         sum = 0
#         continue
#     elif sum < N:
#         print(length-1)
#         break
