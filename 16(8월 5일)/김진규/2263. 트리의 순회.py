# 생각한 방법
# post_order에서 뒤에서 하나씩 앞으로 가면서 in_order에서 해당하는 위치를 찾아 분할 정복
# 하지만 구현을 어떻게 해야할지 모르겠다...

n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))
tree = [[0, 0] for _ in range(n+1)]
LR = []

def find(lst, x, left, right):
    if left > right:
        return -1
    if left == right:
        return left
    for i in range(left, right+1):
        if lst[i] == x:
            return i
    return -1

if n == 1:
    print(1)
for i in range(n-2, -1, -1):
    if i == n-2:
        pre_val = post_order[-1]
        pre_position = find(in_order, pre_val, 0, n-1)
        # pre_position-1이 -일 때와 pre_position+1이 최댓값을 넘었을 때 예외처리 해야함
        LR.append([[0, pre_position-1], [pre_position+1, n-1], pre_val])
        now_val = post_order[i]
        now_position = find(in_order, now_val, 0, n-1)
        if now_position > pre_position:

            LR.append([[LR[-1][1][0], now_position - 1], [now_position + 1, LR[-1][1][1]], now_val])
            LR[-2][1] = 0
        else:
            LR.append([[LR[-1][0][0], now_position - 1], [now_position + 1, LR[-1][0][1]], now_val])
            LR[-2][0] = 0
    else:
        if now_position > pre_position:
            pre_position = now_position
            pre_val = now_val
            now_val = post_order[i]
            # 오른쪽에서 찾기
            now_position = find(in_order, now_val, LR[-1][1][0], LR[-1][1][1])
            LR.append([[LR[-1][1][0], now_position-1], [now_position+1, LR[-1][1][1]], now_val])
            LR[-2][1] = 0

        else:
            pre_position = now_position
            pre_val = now_val
            now_val = post_order[i]
            # 왼쪽에서 찾기
            now_position = find(in_order, now_val, LR[-1][0][0], LR[-1][0][1])
            LR.append([[LR[-1][0][0], now_position - 1], [now_position + 1, LR[-1][0][1]], now_val])
            LR[-2][0] = 0
print(tree)


