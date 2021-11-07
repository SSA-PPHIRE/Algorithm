'''
경우의 수 > dfs

연료 부족 : 일단 가고 나서 0 미만인지 체크
'''
def dfs(c, oil, cnt):
    global ans
    print(c, oil, cnt, end=' /')
    # 조기종료
    if ans < cnt:
        print('조기종료')
        return

    # oil-1 해야 함
    if oil < 0:
        print('연료부족')
        return

    # 종착역에 도착하면 내림
    if c == w[0]:
        ans = cnt
        print('도착')
        return

    if c != 1:
        dfs(c+1, w[c]-1, cnt+1)
    dfs(c+1, oil-1, cnt)

t = int(input())
for tc in range(1, t+1):
    w = list(map(int, input().split()))
    ans = float('inf')
    dfs(1, w[1], 0)
    print(f'#{tc} {ans}')
