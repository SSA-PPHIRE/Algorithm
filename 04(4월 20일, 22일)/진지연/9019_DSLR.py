'''
a에 도착하는 최소길이를 구하는 문제이므로 bfs
queue에서 꺼낸 값에 연산을 하고 > 결과가 나온 적이 없으면 > queue에 추가하고
'DDLSR' 이런 건 어디다 저장하지.. > 검색해보니 queue에 두개 값을 저장하더라!!
'''


'''
참고..
from collections import deque

def BFS_with_adj_list(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited
  
print(BFS_with_adj_list(graph_list, root_node))

'''
from collections import deque


def bfs(root, target):
    queue.append([root, ''])
    visited = [0 for i in range(0, 10000 + 5)]
    while queue:
        num, res = queue.popleft()
        if num == target:
            return res
        if visited[(2*num)%10000] == 0:
            visited[(2 * num) % 10000] = 1
            queue.append([(2 * num) % 10000, res+'D'])
        if visited[(num-1)%10000] == 0:
            visited[(num-1)%10000] = 1
            queue.append([(num-1)%10000, res+'S'])

        if visited[int(num / 1000 + num % 1000 * 10)] == 0:
            visited[int(num / 1000 + num % 1000 * 10)] = 1
            queue.append([int(num / 1000 + num % 1000 * 10), res+'L'])
        if visited[int(num / 10 + num % 10 * 1000)] == 0:
            visited[int(num / 10 + num % 10 * 1000)] = 1
            queue.append([int(num / 10 + num % 10 * 1000), res+'R'])

T = int(input())
for tc in range(T):
    rot, tgt = map(int, input().split())
    queue = deque()
    ans = bfs(rot, tgt)
    print(ans)
