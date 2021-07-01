# 실패
# 접근 방식

'''
1. 삼각형 만들기
2. 숫자 넣어주고
3. 인덱스 활용해서 탐색하면서 값 넣어주기
** 4. 2차원 리스트의 1차원 리스트 화로 정답 추출
https://programmers.co.kr/learn/courses/4008/lessons/12738

my_list = [[1, 2], [3, 4], [5, 6]]

# 방법 1 - sum 함수
answer = sum(my_list, [])

# 방법 2 - itertools.chain
import itertools
list(itertools.chain.from_iterable(my_list))

# 방법 3 - itertools와 unpacking
import itertools
list(itertools.chain(*my_list))

# 방법 4 - list comprehension 이용
[element for array in my_list for element in array]

# 방법 5 - reduce 함수 이용 1
from functools import reduce
list(reduce(lambda x, y: x+y, my_list))

# 방법 6 - reduce 함수 이용 2
from functools import reduce
import operator
list(reduce(operator.add, my_list))

'''

'''
https://greedysiru.tistory.com/466

# 삼각 달팽이
def solution(n):
    # n을 변으로 가지는 이등변직각삼각형 만들기
    triangle = [[0 for i in range(0, j)] for j in range(1, n + 1)]
    # 숫자 채우기
    # 행
    x = -1
    # 열
    y = 0
    # 넣을 수
    k = 1
    # 행 접근
    for a in range(n):
        # 열 접근
        for b in range(a, n):
            if a % 3 == 0:
                x += 1
            elif a % 3 == 1:
                y += 1
            elif a % 3 == 2:
                x -= 1
                y -= 1
            triangle[x][y] = k
            k += 1
    # 1차원 리스트로 변환
    answer = sum(triangle, [])
    return answer

'''


