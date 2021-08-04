'''
1. 
처음에 dfs 로 풀었는데 메모리 초과가 났다.
DP로 풀면 덮어씌우고 덮어씌워서 메모리 초과가 안 난다고 한다.

2.
문제를 제대로 안 읽었다.
세로는 무한정 길어지지만, 가로는 3개임
'''

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
delta = [-1,0,1]


def dfs(r, c, sm):
    global mx, mn
    if r == n-1:
        print('도착했다', sm, mx, mn)
        mx = max(mx, sm)
        mn = min(mn, sm)
        return

    for d in delta:
        new_r = r + 1
        new_c = c + d
        if 0 <= new_r < n and 0 <= new_c < n:
            dfs(new_r, new_c, sm+arr[new_r][new_c])

mx = 0
mn = 9 * n
for i in range(n):
    dfs(0,i,arr[0][i])
print(mx, mn)


#########################

'''
세로는 무한정 늘어나지만 가로는 3으로 고정됨
'''

n = int(input())
next_val = [list(map(int, input().split())) for _ in range(n)]

large = next_val[0]
small = next_val[0]

for i in range(1, n):
    large = [max(large[0], large[1]) + next_val[i][0],
             max(large[0], large[1], large[2])+next_val[i][1],
             max(large[1], large[2]) + next_val[i][2]]
    small = [min(small[0], small[1]) + next_val[i][0],
             min(small[0], small[1], small[2])+next_val[i][1],
             min(small[1], small[2]) + next_val[i][2]]
print(max(large), min(small))
