# 뭔가 투포인터?를 쓰면 좋을 것 같다.
# 문제를 제대로 읽지 않았다...

N, S = map(int, input().split())
lst = list(map(int, input().split()))
l, r = 0, 0
min_len = 1000000
sum_val = 0

while True:
    if sum_val >= S:
        min_len = min(r-l, min_len)
        sum_val -= lst[l]
        l += 1
        if l > r:
            break

    else:
        if r >= N:
            break
        sum_val += lst[r]
        r += 1
# 예외 처리
# S가 0일 땐 min_val이 0으로 나온다.
# sum_val을 -1로 하는게 더 좋아보였는데 시도하니까 틀렸다.
# 생각해보니 그러면 당연히 값이 바뀐다...멍청...
if min_len == 0:
    print(1)
# 만약 S를 넘는 값을 찾지 못한다면 min_len이 1000000가 될 것이므로 0을 출력한다.
elif min_len == 1000000:
    print(0)
else:
    print(min_len)


#########################
# 최초 구현은 엉성했다
N, S = map(int, input().split())
lst = list(map(int, input().split()))
l, r = 0, 0
min_len = 1000000

while True:
    sum_val = 0
    for i in range(l, r+1):
        sum_val += lst[i]
    if sum_val >= S:
        min_len = min(r+1-l, min_len)
        l += 1
        if l > r:
            break
    else:
        r += 1
        if r >= N:
            break

print(min_len)
