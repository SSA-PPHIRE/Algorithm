# 시간초과 뜸
# 인풋받기
k, n = list(map(int, input().split()))
dvds = [int(input()) for i in range(k)]

# upper bound
ub = sum(dvds)//n

# lower bound
if n%k == 0:
    dvs = n//k
else:
    dvs = n//k + 1
lb = min(dvds)//dvs

# for로 돌기
for i in range(lb, ub+1):
    
    cnt = 0
    for dvd in dvds:
        cnt += dvd//i

    if cnt >= 11:
        ans = i
    else:
        print(ans)
        break



        
# 갇힘
# 이런 정렬 이름이 뭐였죠..
def recur(lb, ub):
    # 종료조건
    if lb == ub:
        return ub
    
    # 중간값
    dvs = (lb+ub)//2
    

    cnt = 0
    for dvd in dvds:
        cnt += dvd//dvs

    print(lb, ub, dvs, cnt) #디버깅용

    if cnt >= 11:
        lb = dvs
        recur(lb, ub)
    else:
        ub = dvs
        recur(lb, ub-1)
        
