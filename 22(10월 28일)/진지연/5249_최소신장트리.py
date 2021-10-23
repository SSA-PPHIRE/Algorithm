def find_rep(n):
    while n != rep[n]:
        n = rep[n]
    return n


t = int(input())
for tc in range(1, t + 1):
    V, E = map(int, input().split())
    pairs = [list(map(int, input().split())) for _ in range(E)]
    pairs.sort(key=lambda x: x[2])
    rep = [i for i in range(V + 1)]

    cnt = 1
    weight = 0
    for p in pairs:
        s, e, w = p[0], p[1], p[2]
        # 모든 트리를 돌음
        if cnt == V+1:
            print(f'#{tc} {weight}')
            break
        # 사이클이 돌면 제거
        if find_rep(s) == find_rep(e):
            continue

        rep[find_rep(s)] = rep[find_rep(e)]
        cnt += 1
        weight += w
       
# 참고
'''
if s in visited and e in visited:
-> 각자 다른 사이클을 생성한 후에 최종적으로 합쳐주는 걸 수도 있음! 필요없는 조건

visited를 저장
-> memory 초과됨. cnt를 세는 횟수로만 처리함
'''
t = int(input())
for tc in range(1, t + 1):
    V, E = map(int, input().split())
    pairs = [list(map(int, input().split())) for _ in range(E)]
    pairs.sort(key=lambda x: x[2])
    rep = [i for i in range(V + 1)]

    cnt = 0
    visited = set()
    for p in pairs:
        s, e, w = p[0], p[1], p[2]
        if len(visited) == V + 1:
            print(f'#{tc} {cnt}')
            break
        if find_rep(s) == find_rep(e):
            continue
        if s in visited and e in visited:
            continue

        rep[find_rep(s)] = rep[find_rep(e)]
        visited.add(s)
        visited.add(e)
        cnt += w





