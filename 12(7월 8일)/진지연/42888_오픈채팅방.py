'''
userid의 행동을 순서대로 담는 리스트
userid의 이름을 담은 딕셔너리
'''

def solution(record):
    actions = []
    for r in record:
        actions.append(r.split())
#     print(actions)

    name = {}
    for a in actions:
        if len(a) == 3:
            name[a[1]] = a[2]
#     print(name)

    answer = []
    for r in actions:
        if r[0] == 'Enter':
            answer.append(f"{name[r[1]]}님이 들어왔습니다.")
        elif r[0] == 'Leave':
            answer.append(f"{name[r[1]]}님이 나갔습니다.")

    return answer
