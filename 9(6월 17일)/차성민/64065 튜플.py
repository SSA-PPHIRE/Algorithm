def solution(s):
    answer = []
    # 1. {{    }}  제거
    s = s[2:-2]
    # 2. }와 {를 기준으로 분리하여 제거
    s = s.split("},{")

    # 3. 길이를 기준으로 정렬 (key 속성값 활용)
    s.sort(key=len)

    # 4. 각 문자열을 ,를 기준으로 나누고 int로 형변환 후, 리스트에 추가
    for i in s:
        str1 = i.split(',')
        for j in str1:
            ## 혹시 모르니 예외처리로 리스트 안에 있는지 확인해 줌
            if int(j) not in answer:
                answer.append(int(j))

    return answer
