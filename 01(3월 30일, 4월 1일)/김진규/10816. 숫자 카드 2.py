# 처음에 count를 사용했더니 시간 초과
# 알고리즘 분류에 해쉬를 보고 dict를 이용하기로 결정

N = int(input())
N_lst = list(map(int, input().split()))
# 딕셔너리를 만들고 입력되는 값이 처음 들어왔다면 값에 1을 저장
# 그렇지 않다면 값에 1을 더함
N_dict = {}
for n in N_lst:
    if N_dict.get(n, 0) == 0:
        N_dict[n] = 1
    else:
        N_dict[n] += 1
M = int(input())
M_lst = list(map(int, input().split()))
# 결과를 저장할 리스트를 M의 길이 만큼 선언
res = [0] * M
# M_lst의 값을 순서대로 입력하며 N_dict에 존재하면 그 값을 결과 리스트에 저장
# 존재하지 않는다면 결과값에 0을 저장
for i in range(len(M_lst)):
    if N_dict.get(M_lst[i], 0):
        res[i] = N_dict[M_lst[i]]
    else:
        res[i] = 0
print(*res)
