# 시간초과



# 쌓기 전에 가늠을 해본다
n, m, b = map(int, input().split())
arr = []
for i in range(n):
    arr.extend(map(int, input().split()))


# 초기값
mn = min(arr)
mx = max(arr)

mn_expense = 256 * (mx-mn) * 2
ans_h = mn


for h in range(mn, mx+1):
    higher = 0
    lower = 0
    
    for p in arr:
        diff = p-h
        if diff > 0:
            higher += diff
        else:
            lower += diff
    
    # 가능한지 가늠하기
    expense = 0
    if higher + b < lower:
        continue
    else:
        expense += 2*higher - lower
    

    # 비용 중 최소, 그 중에 높은 것 구하기
    if mn_expense > expense:
        mn_expense = expense
        ans_h = h
    elif mn_expense == expense:
        ans_h = h
    

print(mn_expense, ans_h)
        
        
        
