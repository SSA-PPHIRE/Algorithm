#백준 1463 1로 만들기 S3
# 직접 모든 분기를 작성해주려했으나 실패
#점화식 찾아서 간단히 풀 수 있는 문제
#DP(N) = min(DP(N//3)+1, DP(N//2)+1, DP(N-1)+1)
# 혹은 메모이제이션 활용 (미리 100만개 적용)

#가장 깔끔한 코드
N = int(input())
DP = [0 for _ in range(N+1)]

for i in range(2, N+1):
    DP[i] = DP[i-1] + 1

    if i % 2 == 0 and DP[i] > DP[i // 2] + 1:
        DP[i] = DP[i // 2] + 1

    if i % 3 == 0 and DP[i] > DP[i // 3] + 1:
        DP[i] = DP[i // 3] + 1

print(DP[N])

'''
def chk(N):
    global cnt

    if N < 4:
        cnt += 1
        return cnt
    elif N % 3 == 0:
        N = N/3
        cnt += 1
        chk(N)
    else: # 3으로 바로 나뉘어 지지 않을 때
        if (N - 1) % 3 == 0 and int(N/2) %2 != 0: #2로 2번 연속 나누어지면  10 VS 16
            N -= 1
            cnt += 1
            chk(N)
        elif (N - 1) % 3 == 0 and int(N/2) %2 == 0:
            N = N/4
            cnt += 2
            if N == 1:
                return cnt
            chk(N)
        elif int((N-1)/2) % 2 == 0:
            N -= 1
            cnt += 1
            chk(N)
        elif (N - 2) % 3 == 0 and (N % 2) != 0: # 11 vs 14
            N -= 2
            cnt += 2
            chk(N)
        elif (N - 2) % 3 == 0 and (N % 2) == 0:
            N = N/2
            cnt += 1
            if N == 1:
                return cnt
            chk(N)

N = int(input())
# for i in range(1, 50):
cnt = 0
chk(N)
print(cnt)
'''
