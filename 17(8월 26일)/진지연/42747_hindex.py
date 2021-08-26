'''
2번째줄 조건과 5번째 줄에 range 정하는 게 매우 중요했다
1) range의 두번째값을 min(citations)-1로 하면 에러가 난다
  -> max, min이 같을 경우 for문이 돌지 않음
2) min(citations)-2로 하면 에러가 난다
  -> 최소값보다 작은 수를 고려한다.
'''

def solution(citations):
    if max(citations) == 0:
        return 0
    citations.sort(reverse=True)
    
    for h in range(max(citations),0,-1):
        max_h = 0
        for idx in range(len(citations)):
            if citations[idx] >= h:
                max_h += 1
            if max_h == h:
                return max_h
