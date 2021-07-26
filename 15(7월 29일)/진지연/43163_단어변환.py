'''
쌍을 찾고 bfs로 돌린다
bfs 에서 visited 는 ... 먼저 오면 장땡!
늦게 왔다는 건 다르 최단거리가 있다는 거니까
'''

# 쌍을 찾는다
def similar(words):
    similar_dict = {w:[] for w in words}
    n = len(words[0])
    for w in range(len(words)):
        for d in range(w+1, len(words)):
            w1 = words[w]
            w2 = words[d]
            cnt = 0
            for i in range(n):
                if w1[i] != w2[i]:
                    cnt +=1
            if cnt == 1:
                similar_dict[w1].append(w2)
                similar_dict[w2].append(w1)
    return similar_dict

# bfs로 돌린다
from collections import deque


def solution(begin, target, words):
    words.append(begin)

    similar_dict = similar(words)
    visited = []

    stack = deque([])
    stack.append([begin, 0])
    while stack:
        current_w, cnt = stack.popleft()
        visited.append(current_w)
        for w in similar_dict[current_w]:
            if w == target:
                return cnt + 1

            if w not in visited:
                stack.append([w, cnt + 1])

    return 0
