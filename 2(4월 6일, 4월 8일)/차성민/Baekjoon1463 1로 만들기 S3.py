#백준 1463 1로 만들기 S3
# 직접 모든 분기를 작성해주려했으나 실패
#점화식 찾아서 간단히 풀 수 있는 문제
#DP(N) = min(DP(N//3)+1, DP(N//2)+1, DP(N-1)+1)

#1, 2, 3, 1+3, 2+3, 2 * 3, 1 + 2*3, 2 2 2

# 10 - 3(1,3,3 /  4 -  2,1, 2, 2)
# 11 - 1, 3 (4)     12 - 3,2,2   13 - 4,
# 11 - 1,1,3,3 / 1,2,1,2,2,  14 - 2,1,3,2 / 1,1,3,2,2
# 16 - 2,2,2,2   vs 10
#1, 2, 3, 2'2, 2'2+1, 2 3, 2 3+1 , 2'2'2, 3,3, 3,3+1, 3,3+1+1
# 17 - 5(1,2,2,2,2)
# 28 - 2,2,1,2,3   29-1,2,2,1,2,3 6번

N = int(input())
DP = [0 for _ in range()]



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

