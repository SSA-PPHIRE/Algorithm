'''
백준 9663 N-Queen

10  01  10
10  10  01

(1)을 방지하기 위해 순열로 8개 뽑기

(2,3)대각선 기울기가 +-1이면 dfs를 멈춤
'''

n = int(input())

visited = []
arr = []
cnt = 0
def perm(r):
    global cnt

    if r == n:
        cnt += 1
        return

    for c in range(n):
        if c not in visited:
            # 백트래킹 : 이전에 같은 대각선이 있다면 종료
            flag = 1
            for prev_r in range(len(visited)):
                prev_c = visited[prev_r]
                if abs((prev_r - r)/(prev_c - c)) == 1:
                    flag = 0
                    break

            if flag:
                visited.append(c)
                perm(r+1)
                visited.remove(c)

perm(0)
print(cnt)

