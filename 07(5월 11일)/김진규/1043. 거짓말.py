# 무리의 수 구하기처럼 풀었다!
# 뭔가 엄청 더럽게 짰는데 통과되서 이상했따...

def find(A):
    while True:
        if A == parent[A]:
            break
        else:
            A = parent[A]
    return A


def union(A, B):
    par_A = find(A)
    par_B = find(B)
    if par_A != par_B:
        parent[par_A] = par_B


N, M = map(int, input().split())
people = list(map(int, input().split()))  # 진실을 알고 있는 사람들
people_num = people.pop(0)  # 진실을 알고 있는 사람수
parent = list(range(N+1))  # 무리의 대장(?)을 저장한 리스트
party_lst = []  # 입력되는 파티들을 저장할 리스트

for _ in range(M):
    lst = list(map(int, input().split()))  # 파티를 입력받음
    num = lst.pop(0)  # 파티의 인원수를 따로 꺼낸다.
    party_lst.append(lst[:])  # 파티들을 파티리스트에 넣는다.
    if len(lst) == 1:  # 길이가 1이라면 종속관계가 따로 없으니 생략
        continue
    for i in range(1, num):
        # 길이가 1이상이라면 파티원의 수만큼 반복하며 가장 앞의 사람과 union
        # 어차피 같은 무리에 속할 사람들이므로 누구와 하든 상관없다.
        union(lst[0], lst[i])

# 진실을 알고 있는 사람들을 저장할 set
res = set(people)
# 진실을 알고있는 사람들의 무리의 대장들을 set에 추가
for num in people:
    res.add(find(num))

# 사람 수(1~N+1) 만큼 반복하면서 속한 무리의 대장이 res에 속해있다면 res에 추가
for num in range(1, N+1):
    if find(num) in res:
        res.add(num)

# 거짓말을 할 수 있는 파티의 수
cnt = 0
# 파티들 중 res에 있는 값이 하나라도 있다면 break
# 모두 통과한다면 cnt + 1
for party in party_lst:
    for i in res:
        if i in party:
            break
    else:
        cnt += 1

print(cnt)
