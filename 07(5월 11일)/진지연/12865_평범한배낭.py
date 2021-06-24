'''

https://dojinkimm.github.io/algorithm/2019/10/19/dp-2.html
 knap[i-1, W-w_i] + b_i
 여기서 w_i를 왜 빼는지 모르겠음..
'''


n, limit = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
arr.sort(key=lambda x:x[0], reverse=True)

mx = 0
for i in range(1,2**n+1):
    w = 0
    v = 0
    for j in range(n):
        if i & (1<<j):
            w += arr[j][0]
            v += arr[j][1]
            # 백트래킹
            if w > limit:
                v = 0
                break

    # 최대값
    if mx < v:
        mx = v

print(mx)
