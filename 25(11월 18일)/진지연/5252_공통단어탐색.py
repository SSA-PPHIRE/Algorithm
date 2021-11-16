'''
dict로 하면 더 빠를 듯
'''

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    dictN = {input():1 for _ in range(n)}

    cnt = 0
    for _ in range(m):
        if dictN.get(input()):
            cnt += 1

    print(f"#{tc} {cnt}")

