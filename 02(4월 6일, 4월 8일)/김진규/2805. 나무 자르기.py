# 최근에 했던 이분 탐색을 복습하는 느낌이었다.

N, M = map(int, input().split())
tree_lst = list(map(int, input().split()))
max_val = max(tree_lst)
# 처음에 최솟값을 나무 높이중 최소로 설정햇었었다.
# 그렇게 했더니 모두 같은 높이의 나무는 아예 자르지 않았다.
min_val = 0
# 결과값
res = 0

# 최솟값이 최대값보다 작거나 같을 동안 반복한다.
while min_val <= max_val:
    # 중간값을 구한다.
    mid_val = (max_val + min_val) // 2
    # 자른 나무들의 합을 저장하는 변수를 선언한다.
    sum_val = 0
    # 자른 나무들의 합을 구한다.
    for val in tree_lst:
        if val > mid_val:
            sum_val += val - mid_val
    # 만약 자른 나무들의 합이 M보다 크거나 같다면
    if sum_val >= M:
        # 최솟값을 중간값 + 1로 설정한다.
        min_val = mid_val + 1
        # 결과값보다 중간값이 높다면 결과값에 중간값을 넣는다.
        # 처음엔 자른 나무들의 합이 M과 같을때만 동작하게 했는데
        # 생각해보니 정답이 항상 M과 같이 나오지는 않았다.
        if res < mid_val:
            res = mid_val
    # 그렇지 않다면 최댓값을 중간값 - 1 로 설정한다.
    else:
        max_val = mid_val - 1

print(res)
