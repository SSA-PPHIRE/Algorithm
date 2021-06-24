'''
자기자신보다 작은 소수를 찾는다
n**0.5까지만 해도 됨

백트래킹 : 자기자신보다 크면 건너뛴다

1. 처음에 문제를 잘못 읽었다. 실전에서 이러면 정말 아까울 듯!
2. 원래코드는 왜 안 되는가?
    - list.remove는 시간을 많이 잡아먹는
    - 19, 17이 들어가면 안된다 <- 라는 정보를 활용하지 못함.
'''


# 원래코드
target = int(input())
primes = [i for i in range(2, target+1)]

for p in primes:
    # 제곱근보다 작은 애들만 체크해주면 됨
    if p < target ** 0.5:
        for t in primes:
            if t == p:
                continue
            elif t % p == 0:
                primes.remove(t)

print(primes)
print(len(primes))

# 시작점과 끝점 뽑기
# 큰수부터 더하면 백트래킹이 쉽다
# 문제점 : 19, 17이 들어가면 다 안되는건데 매번 체크하고 있음
cnt = 0
for s in range(len(primes)):
    for e in range(s+1, len(primes)):
        tmp = 0
        for idx in range(e, s-1, -1):
            tmp += primes[idx]
            if tmp > target:
                break
        if tmp == target:
            cnt += 1


if target in primes:
    cnt += 1
print(cnt)



#######################################3

# remove는 시간을 많이 잡아먹음
target = int(input())
chk = [0,0] + [1]*(target-1)
primes = []

for p in range(2, target+1):
    if chk[p]:
        primes.append(p)
        for j in range(p*2, target+1, p):
            chk[j] = False





answer = 0
start = 0
end = 0
while end <= len(primes):
    temp_sum = sum(primes[start:end])
    if temp_sum == target:
        answer += 1
        end += 1
    elif temp_sum < target:
        end += 1
    else:
        start += 1

print(answer)


















