'''
정렬 문제..?  -> X

테케 안되는 질문이 많았음 => h가 배열의 내부 값 중 하나가 아니었음
=> 역순으로 정렬하고 h를 -1하면서 while문 돌리면서 h구하자

sort, sorted, 역정렬, 람다 정렬 좀 더 공부
'''
def solution(citations):
    citations.sort(reverse=True)
    answer = max(citations) #h의 최댓값이 배열의 길이이고, h가 정답이므로 answer에 저장

    while(True): # 찾을때 까지 반복
        count = 0 # h보다 큰 값의 개수
        for i in citations:  # 큰 값 개수 체크
            if i >= answer:
                count += 1
        # 조건이 맞는 가장큰 h값이면 반환
        # (answer번이상 인용된 논문{count}이 answer 이상이고,
        # 나머지 논문{len(citations) - count)이 answer번 이하로 인용 )
        if count >= answer and ( len(citations) - count ) <= answer:
            return answer
        answer -= 1

# citations = [3,0,6,1,5]
# print(solution(citations))
