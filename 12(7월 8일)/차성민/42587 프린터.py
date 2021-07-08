# 중요도가 클 수록 빨리 인쇄, *주의 동일할시에는 보다 큰 중요도의 뒤쪽에 있던 것 우선
# 순서가 0부터 시작

# 리스트쓰고, max로 비교하면 될 듯?

def solution(priorities, location):
    answer = 0
    while(len(priorities)!=0): #while문으로 처리
        if location==0: #맨 앞 순서로 오면
            if priorities[0] < max(priorities): # 큰 우선순위가 있는지 확인
                priorities.append(priorities.pop(0)) # 있으면 맨뒤로 보냄
                location = len(priorities)-1 #location 조정(배열길이의 -1로)
            else: # 더 높은 우선순위가 없으면 이제 출력이 되는 것이므로 +1 후 반환
                return answer + 1
        else:  # 내가 볼게 아니라면
            if priorities[0] < max(priorities):
                priorities.append(priorities.pop(0))
                location -= 1 # 내가 보는게 아닌것이 뒤로 갔으니 한칸 앞으로 이동
            else:
                priorities.pop(0) # 출력
                location -= 1 #한칸 앞으로
                answer += 1 #출력 횟수는 +1됨.

'''
괜찮았던 다른 사람 풀이
deque와 enumerate활용하여 시간 단축

def solution(priorities, location):
  answer = 0
  from collections import deque

  d = deque([(v,i) for i,v in enumerate(priorities)])

  while len(d):
      item = d.popleft()
      if d and max(d)[0] > item[0]:
          d.append(item)
      else:
          answer += 1
          if item[1] == location:
              break
  return answer

'''

