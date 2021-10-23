'''
mn을 float("int")로 설정함
'''
t = int(input())
for tc in range(1, t+1):
    n, a, b = map(int, input().split())

    mn = float("inf")
    for r in range(1, n+1):
        for c in range(1, n+1):
            # 조기종료
            if r*c > n:
                break
            tmp = a*abs(r-c) + b*(n - r*c)
            mn = min(mn, tmp)
    print(f'#{tc} {mn}')
