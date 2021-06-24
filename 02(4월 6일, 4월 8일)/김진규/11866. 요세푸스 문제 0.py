# 풀이를 다 끝내고 다른 사람들의 코드를 보니
# 배열로 선언하면 pop과 append보다 쓸데없는 반복이 생김


N, K = map(int, input().split())
# idx가 0일때는 0 나머지는 1로 저장
yo_lst = [0] + [1]*N
# 모두 0일때와 비교할 리스트
compare_lst = [0]*(N+1)
cnt = 0
idx = 1
res = []
# 리스트가 모두 0일 때 반복을 끝냄
while yo_lst != compare_lst:
    # idx 값을 1 씩 증가하면서 cnt가 K가 되면
    # yo_lst[idx] 값을 0으로 바꾸고
    # 결과 값에 idx를 추가
    # 다시 cnt를 0으로 바꾼 후 반복
    # idx가 N보다 커진다면 idx에 다시 1을 저장
    if yo_lst[idx] == 1:
        cnt += 1
    if cnt == K:
        cnt = 0
        yo_lst[idx] = 0
        res.append(idx)
    idx += 1
    if idx > N:
        idx = 1
print('<', end='')
for i in range(len(res)):
    if i == len(res)-1:
        print(res[i], end='>')
    else:
        print(res[i], end=', ')
