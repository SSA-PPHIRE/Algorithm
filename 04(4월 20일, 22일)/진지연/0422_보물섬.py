'''
백준 0422 보물섬

모든 점에서 bfs
그중에서 가장 큰 값을 반환

바다는 -1, 육지는 0로 해서 dist 행렬을 만든다
0인 모든 스팟에서 bfs 돌릴거다
bfs는 제일 마지막 게 제일 긴 거니까 걔를 반환하면 됨 

unboundedlocalerror 떴음
전역변수에 global 안 해주면 뜬다는데.. 못 찾겠

=> UnboundLocalError: local variable 'x' referenced before assignment
변수 선언전에 불러와서 문제가 생긴 것입니당

bfs에서 longest를 반환할 때 while 문이 한번도 실행되지 않는다면
longest라는 변수는 존재하지 않게 되므로 오류가 발생합니당

while deq와 dist[root_r][root_c] 사이에 longest = 0 추가하고 실행하니까 통과합니당😁

다 읽고 이해하셨으면 수정할 때 이 글도 함께 지워주세용~

'''
from collections import deque
from copy import deepcopy


def strtoint(x):
    if x == 'W':
        return -1
    else:
        return 0


def bfs(root_r, root_c):
    global dist
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]

    deq = deque()
    deq.append([root_r,root_c])
    dist[root_r][root_c] = 1
    # print(root_r, root_c, dist)

    while deq:
        r, c = deq.popleft()
        for d in range(4):
            new_r = r + dr[d]
            new_c = c + dc[d]
            if 0 <= new_r < sero and 0 <= new_c < garo:
                if dist[new_r][new_c] == 0:
                    deq.append([new_r, new_c])
                    dist[new_r][new_c] = dist[r][c] + 1
                    longest = dist[new_r][new_c]
                    # print(new_r, new_c, dist)
    return longest


sero, garo = map(int, input().split())
dist_original = []
for i in range(sero):
    lst = list(map(strtoint, list(input())))
    dist_original.append(lst)


ans = 0
for i in range(sero):
    for j in range(garo):
        if dist_original[i][j] == 0:
            # dist를 매번 리셋해주어야 함!        
            dist = deepcopy(dist_original)

            tmp = bfs(i,j)
            if ans < tmp:
                ans = tmp
print(ans-1)




