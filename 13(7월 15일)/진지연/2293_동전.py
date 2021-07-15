'''
DP란 뭘까..
4원 만들기 
= only 1원 + (4-2)원 만들기
= 1 + 2 
'''

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

count_list = [0] * (k + 1)
# x원짜리 동전 하나로 x원을 만드는 경우의 수 = 1
count_list[0] = 1

for coin in coins:
    for target in range(coin, k + 1):
        count_list[target] += count_list[target - coin]

print(count_list[k])
