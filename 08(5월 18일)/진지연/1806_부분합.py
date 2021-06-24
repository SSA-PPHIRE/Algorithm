'''
투포인터로..
0번부터 시작한다
15가 넘을 때까지 담는다
lgt를 저장한다
s를 하나씩 앞으로 옮긴다
15가 안 넘으면
e를 하나씩 앞으로 옮긴다

25%에서 걸렸는데 뭐가 문제인지느 못 알아냈다.


'''


n, l = map(int, input().split())
arr = list(map(int, input().split()))

sum = 0
s = 0
e = 0
lgt = n
while s < n and e < n:
    while sum < l:
        if e >= n:
            break
        sum += arr[e]
        e += 1
        # print(s, e, sum, lgt)
    else:
        if lgt > e-s:
            lgt = e-s
    # print('*****')


    while sum >= l:
        if s >= n:
            break
        sum -= arr[s]
        s += 1
        # print(s, e, sum, lgt)
    if lgt > e - s + 1:
        lgt = e - s + 1
    # if lgt > e - s:
    #     lgt = e - s
    # print('-----')

print(lgt)
