'''
숫자를 만든다
소수인지 확인한다
check에서 n<2일 때 예외처리 안 해서 오류가 났었다
'''
from math import sqrt
from itertools import permutations


def check(n):
    if n < 2:
        return False

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    cnt = 0
    visited = [0,1]
    answer = []
    for i in range(1, len(numbers)+1):
        for p in permutations(numbers, i):
            if int(''.join(p)) in visited:
                continue
            cnt += check(int(''.join(p)))
            visited.append(int(''.join(p)))
            # print(p, cnt)
    return cnt
