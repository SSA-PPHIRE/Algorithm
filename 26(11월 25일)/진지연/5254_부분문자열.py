'''
9/10 맞음 + 런타임에러
'''


t = int(input())

for tc in range(1, t+1):
    n, test = input().split()
    # 부분문자 구하기
    startPointer = 0
    subStrArr = set()
    while startPointer < len(test):
        endPointer = startPointer + 1
        while endPointer < len(test)+1:
            subStrArr.add(test[startPointer:endPointer])
            endPointer += 1
        startPointer += 1

    # 정렬하기
    subStrArr = list(subStrArr)
    subStrArr.sort()
    ans = subStrArr[int(n)-1]
    print(f'#{tc} {ans[0]} {len(ans)}')
