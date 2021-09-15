'''
set에 여러개 추가할 때 update

여러번 훑어야 하지 않는가?
ㄴ. battle[0] == 2인거 다 훑음
'''

def solution(n, results):

    wins, loses = {}, {}
    for i in range(1, n+1):
        wins[i], loses[i] = set(), set()

    for i in range(1, n+1):
        for battle in results:
            if battle[0] == i:
                wins[i].add(battle[1])
            if battle[1] == i:
                loses[i].add(battle[0])
        print(i)
        print('win', wins)
        print('lose', loses)

        for winner in loses[i]:
            wins[winner].update(wins[i])
        for loser in wins[i]:
            loses[loser].update(loses[i])
        print(i)
        print('win', wins)
        print('lose', loses)

    cnt = 0
    for i in range(1, n+1):
        if len(wins[i]) + len(loses[i]) == n-1:
            cnt += 1
    return cnt
