'''
첫글자
'''

t = int(input())

for tc in range(1, t+1):
    a, b = map(int, input().split())
    arrA = [input() for _ in range(a)]
    arrB = [input() for _ in range(b)]

    cnt = 0
    for strB in arrB:
        for strA in arrA:
            if strA.startswith(strB):
                cnt += 1
                break
    print(f'#{tc} {cnt}')
