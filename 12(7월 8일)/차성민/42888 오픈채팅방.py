# 들어오면 메세지 출력, 나가면 메세지 출력
# 닉네임 변경 - 나가고 바꾼 후 다시 입장 or 채팅방에서 변경
# 닉네임 변경후에 이전 이름들이 모두 바뀌어야 함 (나갔다와도 바뀌어야 함)

# 유저 아이디로 구분됨
# 오늘 문제중에서 가장 이해가 어려웠다가 예시보니까 이해됨.
# 딕셔너리 활용을 좀 더 연습해야 될 듯. 시간이 오래걸림 ㅠ

def solution(record):
    answer = []
    dict = {}
    chat = []
    for s in record: #공백 기준으로 나누면서 확인하고 처리
        sentence = s.split(' ')
        if sentence[0] == 'Enter': # 입장했다면
            dict[sentence[1]] = sentence[2] # 키를 ID로 value를 이름으로해서 넣어 주고 문구 출력
            chat.append([sentence[1], "님이 들어왔습니다."]) #뒤에 붙여줄 내용까지 기입
        elif sentence[0] == 'Leave': # 퇴장했다면
            chat.append([sentence[1], "님이 나갔습니다."])
        elif sentence[0] == 'Change': # 닉네임을 변경했다면
            dict[sentence[1]] = sentence[2]  # 키를 ID로 value를 바뀐 이름으로해서 넣어 줌
    '''
    현재까지 dict : {'uid1234': 'Prodo', 'uid4567': 'Ryan'}
    chat: [['uid1234', '님이 들어왔습니다.'], ['uid4567', '님이 들어왔습니다].....   
    이런 형태 이므로 이제 유저의 ID에 맞게 이름을 넣어주면 끝
    '''
    for c in chat:
        answer.append(dict[c[0]] + c[1]) # 유저의 ID에 맞는 이름과 뒤의 문구를 합친 것을 answer에 추가

    return answer

# record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
# print(solution(record))