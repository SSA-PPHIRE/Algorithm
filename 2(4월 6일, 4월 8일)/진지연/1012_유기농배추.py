T = int(input())

# 인풋 받아서 배추밭 만들기
rows, cols, total = map(int, input().split())
# 배추 심은 위치를 미리 저장해서 얘만 탐색하도록 함 
hereis = []
arr = [[0]*cols for i in range(rows)]
for i in range(total):
    row, col = map(int, input().split())
    hereis.append([row, col])
    arr[row][col] = 1

print('배추있음 hereis', hereis)
print('배추밭 arr', arr)



dr = [-1,0,1,0]
dc = [0,1,0,-1]
bug = 0
visited = []
# 배추의 위치를 검사
# 델타탐색 > 1인 것 발견 > not in visited > visited에 추가, hereis에서 삭제 > 이동
#                   > in visited > 무시
#                   > 9시까지 다 탐색했는데 1이 없다 > +1

visited.append(hereis[0])
print('돌기 전 visited', visited)

r = visited[0][0]
c = visited[0][1]

while hereis:
    for i inrange(4):
        new_r = r + dr[i]
        new_c = c + dr[i]
        if (0 <= new_r < rows) & (0 <= new_c < cols):
            if arr[new_r][new_c] == 1:
                if [new_r, new_c] not in visited:
                    visited.append([new_r, new_c])
                    hereis.remove([new_r, new_c])
                    r = new_r
                    c = new_c
                    break
                if [new_r, new_c] in visited:
                    pass
            else:   # 0이 아닌데 심지어 9시 방향이다
                if i == 3:
                    bug += 1
                

print(bug)






