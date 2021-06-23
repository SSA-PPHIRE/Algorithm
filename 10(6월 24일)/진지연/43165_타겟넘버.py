# https://programmers.co.kr/learn/courses/30/lessons/43165

# 프로그래머스에서도 함수 밖에 선언해도 되더이당~
# cnt는 함수 밖에 선언해서 global로
# numbers, target은 계속 받아와야 하므로 인자로 넣었다


cnt = 0
def dfs(numbers, target, i, pre_sum):
    global cnt
    if i == len(numbers):
        if pre_sum == target:
            cnt += 1
        return
    dfs(numbers, target, i + 1, pre_sum + numbers[i])
    dfs(numbers, target, i + 1, pre_sum - numbers[i])

def solution(numbers, target):
    dfs(numbers, target, 0,0)
    return cnt
