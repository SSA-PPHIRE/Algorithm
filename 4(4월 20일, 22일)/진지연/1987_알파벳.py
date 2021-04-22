'''
1987 알파벳

dfs에서 collected에 TF 수정/취소하는 거
왜 저기 들어가야 하는지??
'''
########################################################

dx = [-1,0,1,0]
dy = [0,-1,0,1]





def BFS(x,y):
    global answer
    q = set([(x,y,board[x][y])])      ### set으로 묶어줘야 함

    while q:
        x,y,ans = q.pop()
        # print(x,y,ans)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<R and 0<=ny<C and board[nx][ny] not in ans:
                q.add((nx,ny,ans+board[nx][ny]))
                answer = max(answer, len(ans)+1)

R,C = map(int, input().split())
board = [[*input()] for i in range(R)]

answer = 1
BFS(0,0)
print(answer)


#########################################################



dr = [-1,1,0,0]
dc = [0,0,-1,1]

def DFS(r,c, cnt):
    global mx

    mx = max(mx, cnt)
    collected.append(arr[r][c])

    for i in range(4):
        new_r = r + dr[i]
        new_c = c + dc[i]
        if 0 <= new_r < row and 0 <= new_c < col:
            if arr[new_r][new_c] not in collected:
                # collected.append(arr[new_r][new_c])
                DFS(new_r,new_c, cnt+1)
                # collected.remove(arr[new_r][new_c])
    collected.remove(arr[new_r][new_c])


row, col = 2, 4
arr = [['C', 'A', 'A', 'B'], ['A', 'D', 'C', 'B']]

collected = []
mx = 1

DFS(0,0,1)
print(mx)


