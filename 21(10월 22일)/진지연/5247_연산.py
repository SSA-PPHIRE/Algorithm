
from collections import deque

def get_answer(N, M):
    min_cnts = {N: 0}
    q = deque()
    q.append((N,0))

    while q:
        num, cnt = q.popleft()
        for i in range(4):
            if i == 0:
                new_num = num + 1
            elif i == 1:
                new_num = num - 1
            elif i == 2:
                new_num = num * 2
            else:
                new_num = num - 10

            if new_num > 1000000:
                continue
            if not min_cnts.get(new_num):
                min_cnts[new_num] = cnt + 1
                q.append((new_num, cnt+1))
            if new_num == M:
                ans = cnt + 1
                return ans
            

t = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split())
    answer = get_answer(N, M)
    print(f'#{tc} {answer}')


