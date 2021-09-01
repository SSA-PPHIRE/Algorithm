'''
https://programmers.co.kr/learn/courses/30/lessons/49189
인접 딕셔너리를 만든다
{
 1:2,3
 2:1,4,5
 3:1,2,4,6
 4:2,3
 5:2
 6:3
}

bfs로 접근한다
visited
cnt 몇인지도
시간초과 뜸
'''

def bfs(connected, n):
    visited = [1]
    distances = [0]
    q = [[1, 0]]
    while len(visited) != n:
        s, dist = q.pop(0)
        print(s, dist)
        for e in connected[s]:
            if e in visited:
                continue
            q.append([e, dist + 1])
            distances.append(dist + 1)
            visited.append(e)
    return distances


def solution(n, edges):
    connected = {i: [] for i in range(1, n + 1)}
    for edge in edges:
        connected[edge[0]].append(edge[1])
        connected[edge[1]].append(edge[0])

    distances = bfs(connected, n)

    return distances.count(distances[-1])
