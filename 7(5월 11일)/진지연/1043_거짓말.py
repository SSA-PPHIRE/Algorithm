'''
대표 노드를 연결

진실러를 연결한다

파티를 순회한다
    해당 파티에 진실러가 있나?
        있으면 파티 사람들을 진실러로 만든다
        없으면 파티 사람들을 연결한다.
            대표 노드의 횟수에 다른 사람들의 횟수를 모두 더한다.
            대표 노도의 횟수에 +1 을 한다

모든 파티가 끝나면 대표 노드를 추린다.
진실러가 아니면서, 자기 자신이 대표노드인 곳의 횟수를 합한다

---
~~~ 이걸로 풀었다 ~~~ (6% 에러)
파티를 순회한다
    파티 사람들을 연결한다
        if rep(i) != rep(i+1):
            p[rep(i)] = rep(i+1)
            cnts[rep(i+1)] += cnts[rep(i)]

모든 파티가 끝나면 대표 노드를 추린다.
진실러 그룹을 찾는 rep(know[1])
진실러가 아니면서, 자기 자신이 대표노드인 곳의 횟수를 합한다
'''

# 초기값
people, nums = map(int, input().split())
p = [i for i in range(people+1)]
cnts = [0]*(people+1)
# print('대표노드들', p)
# print('횟수들', cnts)

def rep(x):
    while x != p[x]:
        x = p[x]
    return x


know = list(map(int, input().split()))줌
# 0이면 know[1]이 없음 
if know[0] == 0:
    know.append(0)

# 진실러들끼리 연결해
for i in know[1:]:
    p[i] = know[1]
# print(p)

parties = [list(map(int, input().split())) for i in range(nums)]
for party in parties:
    n = party[0]
    if n == 1:
        cnts[rep(party[1])] += 1
    else:
        for i in range(1, n):
            if rep(party[i]) != rep(party[i+1]):
                p[rep(party[i])] = rep(party[i+1])
                cnts[rep(party[i+1])] += cnts[rep(party[i])]

true = rep(know[1])
# print(p)
# print(cnts)
# print(know[1], true)
# print('----')
cnt = 0
for i in range(people):
    if i == p[i]:
        # 진실러에 해당하는 건 더하면 안됨 
        if i != true:
            # print(i, cnts[i])
            cnt += cnts[i]
print(cnt)




