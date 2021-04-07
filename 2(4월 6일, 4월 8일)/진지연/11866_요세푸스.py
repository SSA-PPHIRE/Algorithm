'''
반례. 마지막 사람을 지우는 경우
'''


n, jump = map(int, input().split())
arr = [i for i in range(1,n+1)]
ans = []
pointer = 0


while arr:
    pointer = (pointer + jump)%len(arr) -1
    if pointer == -1:
        ans.append(arr.pop(pointer))
        pointer = len(arr)
    else:
        ans.append(arr.pop(pointer))

print('<', end='')
for i in range(n):
    if i == n-1:
        print(ans[i], end='')
    else:
        print(ans[i], end=', ')
print('>')
