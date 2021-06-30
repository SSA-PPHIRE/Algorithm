# https://programmers.co.kr/learn/courses/30/lessons/68645
# 스스로 풀지는 못했지만 좋은 코드를 발견했습니당

# # list comprehension
# word = 'mathematics'
# without_vowels = ''.join([c for c in word if c not in ['a', 'e', 'i', 'o', 'u']])
# # 'mthmtcs'

# non_squars = [x for x in range(101) if sqrt(x)**2 != x]
# # [2, 3, 5, 6, 7, 8, 10, 12, 13, 15, 18, 19, 20, 23, 24, 26, 28, 29, 31, 32, 37, 38, 40, 43, 45, 48, 50, 51, 52, 58, 59, 60, 61, 63, 65, 66, 72, 73, 75, 76, 77, 78, 80, 82, 87, 89, 92, 94, 95, 96, 97]


## 문제 풀이
from itertools import chain
def solution(n):
    maps = [[0 for _ in range(n)] for _ in range(n)]
    y, x = -1, 0
    number = 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                y += 1
            elif i % 3 == 1:
                x += 1
            elif i % 3 == 2:
                y -= 1; x -= 1
            maps[y][x] = number
            number += 1
    result = [i for i in chain(*maps) if i != 0]
    return result
