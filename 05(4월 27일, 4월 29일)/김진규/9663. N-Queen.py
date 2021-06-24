def check(n):
    # n은 현재 행의 index
    global cnt
    # 만약 n이 N이라면 1증가하고 리턴
    if n == N:
        cnt += 1
        return
    # 0~N까지 i는 열의 index
    for i in range(N):
        # i열을 방문하지 않았고
        # n+i가 오른쪽 위 대각선에 포함되지 않고
        # n-i가 왼족 위 대각선에 포함되지 않았다면
        if M_lst[i] == 0 and (n+i) not in r_diagonal and (n-i) not in l_diagonal:
            # 모두 방문 표시를 하고 다음 index를 실행
            M_lst[i] = 1
            r_diagonal.append(n+i)
            l_diagonal.append(n-i)
            check(n+1)
            # 모두 방문 해제
            M_lst[i] = 0
            r_diagonal.pop()
            l_diagonal.pop()


N = int(input())
# 방문 열을 저장할 리스트
M_lst = [0]*N
# 오른쪽 위 대각선
r_diagonal = []
# 왼쪽 위 대각선
l_diagonal = []
# 총 갯수
cnt = 0
# 재귀함수 시작
check(0)
print(cnt)
