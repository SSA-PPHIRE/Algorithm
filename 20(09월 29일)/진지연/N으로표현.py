'''
N을 8번 초과 사용하면 return -1

깍두기: 5, 55, 555, 5555

1번 : 5
2번 : 5+5. 5-5 5*5 5/5 
     (1번 사칙연산)
3번 : 2번 @ 1번, 1번 @ 2번
4번 : 3번 @ 1번, 2번 @ 2번, 1번@3번

'''

def solution(N, number):
    # 허뎝님의 수정 피드백 -> 테스트 케이스가 바뀌면서 예외 사항을 추가해야 함.
    if N == number:
        return 1

    # 1. [ SET x 8 ] 초기화
    s = [set() for x in range(8)]

    # 2. 각 set마다 기본 수 "N" * i 수 초기화
    for i, x in enumerate(s, start=1):
        x.add(int(str(N) * i))

    # 3. n 일반화
    for i in range(1, 8):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i - j - 1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)

        if number in s[i]:
            answer = i + 1
            break

    else:
        answer = -1

    return answer
