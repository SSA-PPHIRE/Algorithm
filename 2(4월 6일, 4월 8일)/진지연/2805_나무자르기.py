'''
나무 자르기의 특징
1) 15일 때 7이 나오면 16일 땐 6이 나오고, 14일 땐 8이상이 나온다.
    즉 완전히 일치하는 답이 있다면 하나만 있다
2) 15일 때 6이 나오고 14일 때 8이 나와서, 7이 안 나올 수는 있다.
    7 이상인 경우 그 중에 최소값을 찾아야 한다
'''

'''
질문
1) 문제풀 때 어떤 식으로 접근하시나요
2) 반례구상 어떻게 하시나요
'''

# 이분탐색
# 시간초과, pypy : 런타임에러

n, target = map(int, input().split())
arr = list(map(int, input().split()))

start = 1
end = max(arr)
# cnt = 0 

while start <= end:       
    mid = (start + end)//2

    # 자르기
    sum_val = 0
    for a in arr:
        if a - mid >0:
            sum_val += a - mid

    # cnt += 1
    # print(cnt, '회 ', start, end, ' 기준 높이는 ', mid, '잘린 것 합은', sum)

    # 목표와 비교하기
    # 목표치보다 작다 > 더 많이 얻어야 한다 > 높이를 낮춘다 = end를 낮춘다

    # 적어도 m미터
    if sum_val == target:
        ans = mid
        break

    if sum_val < target :
        end = mid - 1 
    elif sum_val > target:
        start = mid + 1
        ans = mid

print(ans)
