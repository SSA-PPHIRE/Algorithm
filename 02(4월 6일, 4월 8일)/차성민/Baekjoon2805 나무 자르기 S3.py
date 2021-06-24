#백준 2805 나무 자르기 S3
# 이분 탐색

#pypy3 정답, python 실패
import sys
sys.stdin = open('2805.txt', 'r')
# 나무 M미터 필요
# 높이 지정후 한줄에 연속해있는 나무 절단


N, M = map(int, input().split())
arr = list(map(int, input().split()))
# arr = [0] * N
# for i in range(N):
#     arr[i] = int(stdin.readline())

h = max(arr)
l, r = 0, h   #left, right
while (l <= r):
    sum = 0
    c = (l + r) // 2 #중앙 지점
    for i in arr:
        if i - c > 0:
            sum += (i - c)
        else:
            continue
    if sum >= M: # 최소 조건 만족시
        l = c + 1 # 더 높은 높이가 있을 수 있으므로
    else: #조건 만족을 못할 시
        r = c - 1
print(r)

# 시간 초과 1
# while True:
#     sum = 0
#     for i in arr:
#         if i - h > 0:
#             sum += (i-h)
#         else:
#             continue
#     if sum >= M:
#         print(h)
#         break
#     else:
#         h -= 1
#         continue



