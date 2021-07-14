#백준 2293 동전 1 S1

'''
어려워...
점화식 못 찾아서 실패

다른 풀이

1원만으로 하는 경우  (dp[k] = 1)
-> 1,2원 사용하는 경우는 (1. 2원 포함 X - 위의 경우에 포함됨, 2. 2원을 포함하는 방법 dp[k-2])

=> P원짜리 동전을 추가하면 dp[k] += dp[k-p]가 됨.


from sys import stdin

n, k = map(int, stdin.readline().split())

coins = []
for _ in range(n):
    coins.append(int(stdin.readline()))

count_list = [0] * (k + 1)
# x원짜리 동전 하나로 x원을 만드는 경우의 수 = 1
count_list[0] = 1

for i in coins:
    for j in range(i, k + 1):
        count_list[j] += count_list[j - i]

print(count_list[k])

'''