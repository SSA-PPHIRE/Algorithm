'''
순열로 돌리고, 각각을 소수체크
- 에라토스테네스 + 제곱근 소수체크? 에라토스를 쓸 이유가 없음.(느릴 듯)
- 일반 소수체크 X
- 제곱근 소수체크  가능은 할듯?

Key : 중복체크, 소수 판정, 제곱근활용(속도)
'''

from itertools import permutations
import math

def is_prime(num):
    if num < 2:  # 2미만이면 소수 아니까 먼저 확인
        return False

    for i in range(2, int(math.sqrt(num))+1): # 속도측면에서 제곱근 활용(소수점일 수 있으니 +1)
        if num % i == 0:
            return False
    return True

def solution(numbers):

    answer = [] #0을 쓰려했으나 아래 * 부분 때문에 []를 써줘야했음

    for num in range(1, len(numbers)+1):
        arr = list(map(''.join, permutations(list(numbers), num))) #순열 돌리기 (1자리, 2자리 ...순으로)
        arr = list(set(arr))  # 중복 1차 제거

        for i in arr:
            if is_prime(int(i)):
                answer.append(int(i))

    answer = len(set(answer))#*부분: 중복제거를 위에서 해서 끝이라 생각했는데 생각해보니 0땜시 자리수가 달라도 같은값이 될 수 있어서

    return answer
