#백준 9019 DSLR G5
# 파이썬 - 시간초과, pypy3 - 통과

# 문제 유형 파악이 어려웠음 (BFS)
# 신경써줘야하는 부분들이 너무 많음. + 시간초과 압박까지 (파이썬에서는 어떻게 시간 맞출 수 있는가..)

# Key : 최소한의 명령어 나열 how? : visited 확인하며 진행
# 입력받은 A 큐에 넣고 bfs 진행


from collections import deque
import sys
sys.stdin = open('text/9019.txt', 'r')

def BFS(a):
    q = deque()
    q.append([a, ''])  # 첫 값, operator 의 구조로 만들고 operator부분 출력.

    visited = [0] * 10000 # 0 ~ 9999 이므로
    visited[a] = 1

    while q:
        val, operator = q.popleft()

        if val == b: #b와 같으면 return
            return operator

        # LL과 RR의 결과가 같을 때와 같은 상황에서 우선으로 특정 문자를 출력할 조건은 없었으므로 d,s,l,r 순으로 진행

        if not visited[val * 2 % 10000]: # D: 2배 9999보다 크면 10000으로 나눈 나머지 취함 % 10000
            visited[val * 2 % 10000] = 1
            q.append([val * 2 % 10000, operator + "D"])

        if not visited[(val - 1) % 10000]: # S: n-1결과 저장 0이면 -> 9999
            visited[(val - 1) % 10000] = 1
            q.append([(val - 1) % 10000, operator + "S"])

        #L과 R은 변환시 자리수가 유지 되도록 신경 써줘야 했음.
        if not visited[val % 1000 * 10 + val // 1000]: #L: n의 각 자리수를 왼편으로 회전 시키고 저장 d2 d3 d4 d1
            visited[val % 1000 * 10 + val // 1000] = 1
            q.append([val % 1000 * 10 + val // 1000, operator + "L"])

        if not visited[val % 10 * 1000 + val // 10]: # R: n의 각 자릿수를 오른편으로 회전 시키고 저장 d4 d1 d2 d3
            visited[val % 10 * 1000 + val // 10] = 1
            q.append([val % 10 * 1000 + val // 10, operator + "R"])

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(BFS(a))



