'''
최단거리 구하는 문제이므로 bfs 활용

탐색하는 순서
1) 상좌우하 델타탐색하면서 queue에 넣는다
    이때 큰 물고기가 있으면 queue에 넣을 수 없다
2) 물고기가 있으면 거기서 탐색한다
    (queue와 visited를 초기화하고 1번부터 다시 시작함)
3) 물고기가 없으면 queue에서 델타탐색한다

RecursionError: aximum recursion depth exceeded in comparison


'''



dr = [-1,0,0,1]
dc = [0,-1,1,0]


visited = []
def bfs(r,c, shark, ate):
    global arr, q, time
    q = [[r,c]]
    visited = [[r,c]]

    while q:
        r, c = q.pop(0)

        for i in range(4):
            new_r = r + dr[i]
            new_c = c + dc[i]

            if 0 <= new_r < n and 0 <= new_c < n and [new_r, new_c] not in visited:
                visited.append([new_r, new_c])
                q.append([new_r, new_c])

                # 물고기가 크면 지나갈 수 없다
                if arr[new_r][new_c] > shark:
                    visited.remove([new_r, new_c])
                    continue

                # 물고기가 작으면 잡아먹고, 몸집 불리고, 후보들 다 지우고, 거기로 이동한다
                elif arr[new_r][new_c] < shark:
                    q.append([new_r, new_c])
                    arr[new_r][new_c] = 0
                    ate += 1
                    if ate == shark:
                        shark += 1

                    # time
                    time += abs(new_r - r) + abs(new_c - c)

                    q = []
                    visited = []
                    bfs(new_r, new_c, shark, ate)

                    
                    
n = 3
arr = [[0,0,0], [0,0,0], [0,9,0]]              
                    
time = 0
bfs(2,1,2,0)
print(cnt)
