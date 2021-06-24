#백준 10816 숫자 카드 2 S4
#시간초과에 유의해야하는 문제
#딕셔너리 활용 풀이

import sys
sys.stdin = open('10816.txt', 'r')

N = int(input())
nums = list(map(int, input().split())) #상근이가 가진 숫자 카드리스트

M = int(input())
nums2 = list(map(int, input().split())) #비교하려하는 카드 리스트

dic = {} #딕셔너리 생성

for num in nums:  #각 수와, 개수를 딕셔너리안에 저장
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1

for num2 in nums2: #비교하려는 카드 리스트의 각 수들이 딕셔너리 안에 있으면 출력하고 없으면 0 출력
    if num2 in dic:
        print(str(dic[num2]), end=' ')
    else:
        print('0',end= ' ')


# 일차 풀이  (2중 for문 => 시간 초과)
# for i in nums2:
#     cnt = 0
#     for j in nums:
#         if i == j:
#             cnt+=1
#     print(cnt, end=' ')