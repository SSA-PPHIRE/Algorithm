# 방문체크의 중요성을 느낄 수 있었다
# 맞게 구현했는데 시간 초과와 메모리 초과의 대 환장 파티
# 방문체크 추가 후 바로 통과
# 하지만 매우 아슬아슬함 더 좋은 풀이법은 없나?
# 게시판 형님들은 대단하시다


from collections import deque
# 체크할 순서대로 문자 추가
str_lst = ['D', 'S', 'L', 'R']


# bfs
def dslr(tar, pur):
    # q1에 변경할 대상인 숫자를 추가
    q1 = [tar]
    # q2에 문자열을 더해갈 '' 추가
    q2 = ['']
    # 둘다 deque으로 선언 => popleft를 쓰기 위해
    q1 = deque(q1)
    q2 = deque(q2)
    while True:
        val = q1.popleft()
        tmp_str = q2.popleft()

        for i in range(4):
            # 원래 값이 변경되는 것을 막기위해 num에 val 저장
            num = val
            # i == 0 일 때 D
            if i == 0:
                num *= 2
                if num >= 10000:
                    num %= 10000
            # i == 1 일 때 S
            elif i == 1:
                num -= 1
                if num == -1:
                    num = 9999
            # i == 2 일 때 L
            elif i == 2:
                last = num // 1000
                first = num % 1000
                num = first * 10 + last
            # i == 3 일 때 R
            else:
                first = num % 10
                last = num // 10
                num = first * 1000 + last
            # 방문체크 됐다면 continue
            if visited[num] == 1:
                continue
            # 목표와 같다면 문자열을 반환
            if num == pur:
                return tmp_str + str_lst[i]
            # 방문체크
            visited[num] = 1
            # 각각의 큐에 추가
            q1.append(num)
            q2.append(tmp_str + str_lst[i])


T = int(input())
for tc in range(1, 1+T):
    A, B = map(int, input().split())
    # 방문 체크를 위한 배열 선언
    visited = [0] * 10000
    print(dslr(A, B))
