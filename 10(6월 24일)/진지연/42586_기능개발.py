# https://programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    remain = []
    for i in range(len(progresses)):
        days = 0
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            days += 1
        remain.append(days)

    
    publish = []
    cnt, pointer = 0, remain[0]
    for i in range(len(remain)):
        # pointer보다 더 큰 수를 만나면
            # 이전까지 cnt한 것을 넣는다
            # cnt를 초기화한다 
            # pointer를 옮긴다
        # 기본적으로는 cnt를 하나씩 증가시킨다
        # 마지막에 다다르면 pointer보다 크지 않더라도 해준다
        if remain[i] > pointer:
            publish.append(cnt)
            cnt = 0
            if i <= len(remain)-1:
                pointer = remain[i]  
        cnt += 1
        if i == len(remain) - 1:
            publish.append(cnt)
        
        
    return publish
