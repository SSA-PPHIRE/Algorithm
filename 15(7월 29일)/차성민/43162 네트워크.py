# 프로그래머스 네트워크 Lv3

'''
유형을 알고 문제를 접하는거와 모르고 접하는거 차이가 상당한듯

DFS, BFS
나는 확실히 DFS가 익숙한 듯.
- 재귀로 하고싶어서 재귀로 함.
'''


def solution(n, computers):
    answer = 0

    def dfs(n, computers, visited, i):  # 이렇게 함수 선언해도 되나했는데 되네
        for j in range(n):
            if visited[j] == 0 and computers[i][j] == 1:  # 방문 X고, 연결 o면
                visited[j] = 1
                dfs(n, computers, visited, j)  # 재귀로 진행행

    visited = [0] * n

    for i in range(n):
        if visited[i] == 0:  # 미방문 했을 시 진행
            dfs(n, computers, visited, i)
            answer += 1  # 연결된

    return answer

# n = 3
# computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# print(solution(n, computers))